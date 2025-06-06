# Scanning the rooms of a single structure

**Framework**: RoomPlan

Create an AR experience that enables people to scan a building that contains multiple rooms.

#### Overview

RoomPlan can combine the data from multiple scan sessions to create a single captured result that includes multiple rooms. Having a single structure object ([`CapturedStructure`](capturedstructure.md)) lets you create a USDZ file and inspect for particular shapes, dimensions, or items that RoomPlan observes in the structure. Scanned structures support rooms with varying floor heights and rooms that reside on different floors in the building.

![A graphical rendering of 3D geometry that rests on a grid. At left, a collection of 3D rooms fan out disparately with a callout that reads Individual scans. At right, the same individual rooms gather and connect tightly to form a complete building, with a callout that reads Merged structure.](https://docs-assets.developer.apple.com/published/bcc381e2eecd6912ff5951ea47b261bb/scan-merging-article-1%402x.png)

To scan a structure, your app guides a person to scan each room in the building, one by one. To start scanning a room, your app calls [`run(configuration:)`](roomcapturesession/run(configuration:).md) on a room-capture session instance ([`RoomCaptureSession`](roomcapturesession.md)). If your app uses the framework-provided view ([`RoomCaptureView`](roomcaptureview.md)) to facilitate scanning, access the view’s [`captureSession`](roomcaptureview/capturesession.md) property. If your app renders its own graphical interface, create and manage the room-capture session directly.

Your app guides a person through the scanning process by presenting informational text on how to move the device through the room. To indicate a room scan is complete, a person interacts with an interface that your app provides, such as tapping the Finish Room button in the toolbar. Your app stops the room-capture session by calling [`stop(pauseARSession:)`](roomcapturesession/stop(pausearsession:).md), passing an argument of `false` to keep the session open, as required to scan another room.

Each time your app calls `stop(pauseARSession:)`, the system invokes your app’s [`captureSession(_:didEndWith:error:)`](roomcapturesessiondelegate/capturesession(_:didendwith:error:)-5f0mc.md) method, in which you process the raw scan results and create a finished [`CapturedRoom`](capturedroom.md). Store each `CapturedRoom` in an array until a person finishes scanning the whole structure.

A person indicates they’re done scanning all the rooms by interacting with an interface your app provides, such as by tapping the Finish Structure button in the toolbar. With the finalized room array, use the framework to merge the rooms into a single structure. Instantiate a ([`StructureBuilder`](structurebuilder.md)) instance and pass the array to the [`capturedStructure(from:)`](structurebuilder/capturedstructure(from:).md) method, which outputs a `CapturedStructure` object.

#### Create a Room Capture Session and Begin a Scan

To capture a structure that contains multiple rooms, scan each room one by one. Start by creating a single `RoomCaptureSession` instance for the first room:

```swift
var myCaptureSession = RoomCaptureSession()
```

If your app runs its own AR experience, you can pass your existing `ARSession` to RoomPlan using the [`init(arSession:)`](roomcapturesession/init(arsession:).md) method. Apps that utilize the framework-provided UI (`RoomCaptureView`) for scanning can hand off the AR session similarly:

```swift
var roomCaptureView = RoomCaptureView(frame:myFrame, 
                                  arSession:existingARSession)
```

Begin the room-capture session by running it with a configuration:

```swift
myCaptureSession.run(configuration: captureSessionConfig)
```

#### Guide a Person By Displaying Instructional Text

As a person holds the device, the framework models the room by analyzing data from the device’s camera and LiDAR Scanner. To enable the device to acquire sufficient data to model the whole room, your app guides a person on how to move and where to point the device.

The framework-provided view automatically presents text instructions that guide a person through the process. If your app renders its own graphical interface, display your own text according to the instructions that [`RoomCaptureSessionDelegate`](roomcapturesessiondelegate.md) provides in its [`captureSession(_:didProvide:)`](roomcapturesessiondelegate/capturesession(_:didprovide:)-5hvhl.md) method. The [`RoomCaptureSession.Instruction`](roomcapturesession/instruction.md) object that the system passes in assists you with crafting the right information to display to someone.

#### Finalize a Room Scan and Keep the Ar Session Running

After a person completes scanning the room, stop the room-capture session. To keep subsequent rooms compatible for merging, make the AR session continue running by calling `stop(pauseARSession:)` with an argument of `false`.

```swift
myCaptureSession.stop(pauseARSession:false)
```

If your app uses framework-provided UI, stop the scan by referencing the view’s room-capture session:

```swift
roomCaptureView.captureSession.stop(pauseARSession:false)
```

When the room-capture session ends, the system calls your delegate’s [`captureSession(_:didEndWith:error:)`](roomcapturesessiondelegate/capturesession(_:didendwith:error:).md) method, which provides the scan results. Create a `CapturedRoom` object from the scan results and store them in an array for later:

```swift
func captureSession(_ session: RoomCaptureSession, 
              didEndWith data: CapturedRoomData,
                        error: Error?) {    
    let roomBuilder = RoomBuilder(options: [.beautifyObjects]
    /// ... 
    let capturedRoom = try? await roomBuilder.capturedRoom(from: data) else { return }
    if let room = capturedRoom {  
        self.roomsArray.append(capturedRoom)
```

Repeat this process until the person captures all the rooms. To start the next scan, call `run(configuration:)` again on the same room-capture session object. For the final room, you can call the regular [`stop()`](roomcapturesession/stop().md) function at the end. However, apps that want to keep the AR experience going after scanning is done can call `stop(pauseARSession:)` with an argument of `false` to keep the AR session open.

For an example app that implements room scanning with the framework-provided UI, see [`Create a 3D model of an interior room by guiding the user through an AR experience`](create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience.md).

During the structure scanning process, your app manages two kinds of sessions: [`RoomCaptureSession`](roomcapturesession.md), and [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession). To successfully merge rooms, each `RoomCaptureSession` needs to share the same common coordinate space as the `ARSession`. The coordinate space is common when:

- The rooms are close to each other (for example, in the same building).
- The captured session utilizes a  AR session or a  AR session.

An `ARSession` is  when a person completes all scans without interruption, or the `RoomCaptureSession` contains the same AR session object that your app maintains after each room scan by calling [`stop(pauseARSession:)`](roomcapturesession/stop(pausearsession:).md) with an argument of `false`.

If the person sends the app to the background or the AR session experiences tracking problems while a person moves room to room, your app needs to  the AR session before continuing to scan. Relocalizing instructs ARKit to restore a common coordinate space by inspecting a world-map ([`ARWorldMap`](https://developer.apple.com/documentation/ARKit/ARWorldMap)) object that you provide.

#### Relocalize an Ar Session After an Interruption

When a person sends the app to the background or restarts the app before finishing the structure, or if ARKit encounters a tracking error, your app has to restart the AR session. By default, new or restarted AR sessions define a coordinate space that’s incompatible with prior runs because the world origin and orientation are different. To scan more rooms that are compatible with prior scans, you need to restore a common coordinate space by using .

To enable relocalization, the following code implements an [`ARSessionObserver`](https://developer.apple.com/documentation/ARKit/ARSessionObserver) and responds to its [`sessionShouldAttemptRelocalization(_:)`](https://developer.apple.com/documentation/ARKit/ARSessionObserver/sessionShouldAttemptRelocalization(_:)) callback:

```swift
func sessionShouldAttemptRelocalization(_ session: ARSession) -> Bool { return true }
```

When you enable relocalization, ARKit automatically informs your app when it’s time to restore the prior coordinate space by setting the camera tracking state to [`ARCamera.TrackingState.limited(_:)`](https://developer.apple.com/documentation/ARKit/ARCamera/TrackingState-swift.enum/limited(_:)) with reason  [`ARCamera.TrackingState.Reason.relocalizing`](https://developer.apple.com/documentation/ARKit/ARCamera/TrackingState-swift.enum/Reason/relocalizing). The following code responds to this tracking-status change:

```swift
func session(_ session: ARSession, cameraDidChangeTrackingState camera: ARCamera) {
    respondToStatusChange(for: session.currentFrame!, trackingState: camera.trackingState)
}
```

When the tracking-state reason is `.relocalizing`, ask the person scanning to return to their prior location in the physical environment where the interruption occurred. The following code conveys this request by displaying a label that tells people what to do:

```swift
private func respondToStatusChange(for frame: ARFrame, trackingState: ARCamera.TrackingState) {
// ...
case (.limited(.relocalizing), _) where isRelocalizingMap:
    message = "Move your device to the most recently scanned room."
    snapshotThumbnail.isHidden = false
```

As ARKit processes the camera feed, it identifies similarities in an [`ARWorldMap`](https://developer.apple.com/documentation/ARKit/ARWorldMap) object, which acts as the session’s memory of where the scan left off. When ARKit recognizes the environment, it reorients itself, which completes the relocalization process. ARKit sets the camera tracking status to `normal`, and your app resumes scanning.

Your app manages the `ARWorldMap` object that acts as the session’s memory. For a complete example app that demonstrates relocalization using an `ARWorldMap`, see [`Saving and loading world data`](https://developer.apple.com/documentation/ARKit/saving-and-loading-world-data).

With the relocalized `ARSession` object, you can resume scanning the rest of the structure by creating a new room-capture session with the `init(arSession:)` intializer:

```swift
var roomCaptureSession = RoomCaptureSession(arSession:relocalizedARSession)
```

#### Merge the Rooms to Create the Structure

After you collect all of the captured rooms in an array, hand it off to the [`capturedStructure(from:)`](structurebuilder/capturedstructure(from:).md) method of [`StructureBuilder`](structurebuilder.md) to create the [`CapturedStructure`](capturedstructure.md) instance, as the following code demonstrates:

```swift
// Access the newly captured structure.
let capturedStructure = structureBuilder.capturedStructure(from: capturedRoomArray)
```

For a complete example app that merges a collection of prescanned rooms, see [`Merging multiple scans into a single structure`](merging-multiple-scans-into-a-single-structure.md).

## See Also

- [Merging multiple scans into a single structure](merging-multiple-scans-into-a-single-structure.md)
  Export a 3D model that consists of multiple rooms captured in the same physical vicinity.
- [struct CapturedRoom](capturedroom.md)
  A structure that provides the key details of a scanned room.
- [struct CapturedStructure](capturedstructure.md)
  An object that holds the results of the merger of multiple capture sessions.
- [struct CapturedRoomData](capturedroomdata.md)
  An opaque object that holds the raw results of a scan.
- [Captured Object Attributes](captured-object-attributes.md)
  Determine details about the objects and surfaces that the framework identifies in a scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/scanning-the-rooms-of-a-single-structure)*
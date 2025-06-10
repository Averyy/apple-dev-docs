# DockAccessory

**Framework**: DockKit  
**Kind**: class

Obtain accessory information and control tracking behavior.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final class DockAccessory
```

#### Overview

`DockAccessory` provides information about the dock accessory including its model name and firmware version. It also controls the dock accessory when you disable system tracking. Use `DockAccesory` to  perform animations, or explicitly control the position of the dock accessory in three-dimensional space by supplying coordinates in units of radians.  The collection of the X, Y, and Z values corresponding to pitch, yaw, and roll is the  of the dock accessory.

If there are multiple subjects in a video frame, direct the dock accessory to focus on a particular area of the frame using [`setFramingMode(_:)`](dockaccessory/setframingmode(_:).md).

> ❗ **Important**: DockKit throws a [`DockKitError.frameRateTooHigh`](dockkiterror/frameratetoohigh.md) exception if you animate or set the orientation of the dock accessory too quickly, so keep call rates at 2 times per second or less.

## Topics

### Selecting and tracking
- [func selectSubject(at: CGPoint) async throws](dockaccessory/selectsubject(at:).md)
  Selects a subject to track at the supplied coordinates.
- [func track([AVMetadataObject], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-4yl9b.md)
  Automatically generate and send tracking vectors to the device.
- [func track([DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation) async throws](dockaccessory/track(_:camerainformation:)-44mwn.md)
  Automatically generate and send tracking vectors to the device.
- [DockAccessory.Observation](dockaccessory/observation.md)
  An observation of the contents of a single video frame.
- [DockAccessory.CameraInformation](dockaccessory/camerainformation.md)
  A collection of tracking information about the camera currently in use.
- [DockAccessory.CameraOrientation](dockaccessory/cameraorientation.md)
  The set of camera orientations used to extract coordinates.
### Performing animation
- [func animate(motion: DockAccessory.Animation) async throws -> Progress](dockaccessory/animate(motion:).md)
  Starts an animation sequence.
- [func setRegionOfInterest(CGRect) async throws](dockaccessory/setregionofinterest(_:).md)
  Sets the area in the video frame in which the dock accessory tracks a subject.
- [var regionOfInterest: CGRect](dockaccessory/regionofinterest.md)
  The area in the video frame in which the dock accessory tracks a subject.
- [DockAccessory.Animation](dockaccessory/animation.md)
  Character animations that describe how to move the dock accessory.
### Setting position and limits
- [func setLimits(DockAccessory.Limits) throws](dockaccessory/setlimits(_:).md)
  Sets limits for the axes of rotation.
- [func setOrientation(Vector3D, duration: Duration, relative: Bool) throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-2epe2.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func setOrientation(Rotation3D, duration: Duration, relative: Bool) throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-6b0fl.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func setAngularVelocity(Vector3D) async throws](dockaccessory/setangularvelocity(_:).md)
  Sets the angular velocity of each axis of orientation.
### Setting framing mode
- [func setFramingMode(DockAccessory.FramingMode) async throws](dockaccessory/setframingmode(_:).md)
  Customize the dock accessory’s tracking behavior.
- [var framingMode: DockAccessory.FramingMode](dockaccessory/framingmode-swift.property.md)
  The current framing mode.
- [DockAccessory.FramingMode](dockaccessory/framingmode-swift.enum.md)
  The mode to control framing of the subject when tracking.
### Getting position and limits
- [var motionStates: DockAccessory.MotionStates](dockaccessory/motionstates-swift.property.md)
  Motion information from the dock accessory that includes current orientation and velocity of all axes.
- [var limits: DockAccessory.Limits](dockaccessory/limits-swift.property.md)
  Current limits for the axes of rotation and maximum angular velocity.
- [DockAccessory.MotionState](dockaccessory/motionstate.md)
  An event that indicates the state of a dock accessory’s current position and speed.
- [DockAccessory.MotionStates](dockaccessory/motionstates-swift.struct.md)
  An asynchronous sequence of orientation and velocity updates from the device.
- [DockAccessory.Limits](dockaccessory/limits-swift.struct.md)
  Soft limits on multiple axes of rotation.
### Getting accessory information
- [var firmwareVersion: String?](dockaccessory/firmwareversion.md)
  The firmware version of the dock accessory.
- [var hardwareModel: String?](dockaccessory/hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](dockaccessory/identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Identifier](dockaccessory/identifier-swift.struct.md)
  Information that uniquely identifies the dock accessory.
- [DockAccessory.Category](dockaccessory/category.md)
  Types of supported dock accesories.
- [DockAccessory.State](dockaccessory/state.md)
  The state of a dock accessory.
- [DockAccessory.StateChange](dockaccessory/statechange.md)
  An event that indicates a change in the state of a dock accessory.
- [DockAccessory.StateChanges](dockaccessory/statechanges.md)
  An asynchronous sequence of dock accessory state changes.
### Inspecting the object
- [func hash(into: inout Hasher)](dockaccessory/hash(into:).md)
  Creates a unique identifier representing the object.
- [var debugDescription: String](dockaccessory/debugdescription.md)
  The text description of the dock accessory state.
### Structures
- [DockAccessory.AccessoryEvents](dockaccessory/accessoryevents-swift.struct.md)
  An asynchronous sequence of dock accessory events.
- [DockAccessory.BatteryState](dockaccessory/batterystate.md)
  A struct that represents an accessory battery state.
- [DockAccessory.BatteryStates](dockaccessory/batterystates-swift.struct.md)
  An asynchronous sequence of dock accessory battery states.
- [DockAccessory.TrackedObject](dockaccessory/trackedobject.md)
  The state of a tracked object in the active tracking session.
- [DockAccessory.TrackedPerson](dockaccessory/trackedperson.md)
  The state of a tracked person in the active tracking session.
- [DockAccessory.TrackingState](dockaccessory/trackingstate.md)
  A representation of the active tracking session state.
- [DockAccessory.TrackingStates](dockaccessory/trackingstates-swift.struct.md)
  An asynchronous sequence of tracking session states.
### Operators
- [static func == (DockAccessory, DockAccessory) -> Bool](dockaccessory/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var accessoryEvents: DockAccessory.AccessoryEvents](dockaccessory/accessoryevents-swift.property.md)
  Events from the accessory that signify button presses or common camera controls.
- [var batteryStates: DockAccessory.BatteryStates](dockaccessory/batterystates-swift.property.md)
  Battery states from the accessory that indicate changes in battery charge or readiness
- [var hashValue: Int](dockaccessory/hashvalue.md)
  The hash value.
- [var trackingStates: DockAccessory.TrackingStates](dockaccessory/trackingstates-swift.property.md)
  Provides an access to the asynchronous sequence of tracking session states
### Instance Methods
- [func selectSubjects([UUID]) async throws](dockaccessory/selectsubjects(_:).md)
  Selects subjects to track with specific identifiers
- [func setOrientation(Rotation3D, duration: Duration, relative: Bool) async throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-6h2ah.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func setOrientation(Vector3D, duration: Duration, relative: Bool) async throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-84z7i.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func track([DockAccessory.Observation], cameraInformation: DockAccessory.CameraInformation, image: CVPixelBuffer) async throws](dockaccessory/track(_:camerainformation:image:)-3uuza.md)
  Automatically generate and send tracking vectors to the device.
- [func track([AVMetadataObject], cameraInformation: DockAccessory.CameraInformation, image: CVPixelBuffer) async throws](dockaccessory/track(_:camerainformation:image:)-82m61.md)
  Automatically generate and send tracking vectors to the device.
### Enumerations
- [DockAccessory.AccessoryEvent](dockaccessory/accessoryevent.md)
  An enumeration that represents an accessory event.
- [DockAccessory.BatteryChargeState](dockaccessory/batterychargestate.md)
  The charging state of an accessory battery
- [DockAccessory.TrackedSubjectType](dockaccessory/trackedsubjecttype.md)
  The subjects that the dock can track.
### Default Implementations
- [Equatable Implementations](dockaccessory/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Controlling a DockKit accessory using your camera app](controlling-a-dockkit-accessory-using-your-camera-app.md)
  Follow subjects in real time using an iPhone that you mount on a DockKit accessory.
- [class DockAccessoryManager](dockaccessorymanager.md)
  Observe the state of dock accessories and enable or disable system tracking.
- [enum DockKitError](dockkiterror.md)
  A list of errors that DockKit sends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory)*
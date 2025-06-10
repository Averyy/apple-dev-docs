# capturedStructure(from:)

**Framework**: RoomPlan  
**Kind**: method

Combines the argument captured rooms into a single unit.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS ?+

## Declaration

```swift
func capturedStructure(from rooms: [CapturedRoom]) async throws -> CapturedStructure
```

## Mentions

- [Scanning the rooms of a single structure](scanning-the-rooms-of-a-single-structure.md)

#### Return Value

An object that consists of all of the captured room data across one or more scan sessions.

#### Discussion

Each captured room in the argument array represents the post-processed result of a single scan session. This function succeeds when all of the captured rooms share compatible world space; otherwise, the function fails with an error. [`CapturedRoom`](capturedroom.md) instances share compatible world space if they reside in the same physical vicinity (they connect to form a larger structure), such as different rooms in the same building.

There are two ways to ensure the captured rooms share compatible world space. You continue a single AR session by:

- Passing the same [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession) instance to the [`RoomCaptureSession`](roomcapturesession.md) objects that each produce a captured room. Be sure to pause the `ARSession` by calling [`stop(pauseARSession:)`](roomcapturesession/stop(pausearsession:).md) with an argument of `false` before handing it to a subsequent room-capture session.
- Loading a previously saved [`ARWorldMap`](https://developer.apple.com/documentation/ARKit/ARWorldMap) to create an `ARSession` in compatible world space with previous scans.

> **Note**: After loading a previously saved `ARWorldMap`, wait for [`ARCamera.TrackingState`](https://developer.apple.com/documentation/ARKit/ARCamera/TrackingState-swift.enum) to change from `relocalizing` to `normal`. For this change to take effect, the system needs to observe through the camera some portion of the recently scanned area. To guide the user accordingly, you can present a UI that instructs the user to return to the previous room before beginning the next room-capture session.

For information about saving and loading world maps to restore an [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession), see [`Saving and loading world data`](https://developer.apple.com/documentation/ARKit/saving-and-loading-world-data).

## Parameters

- `rooms`: An array of captured room objects the app generates by performing multiple room-capture sessions in the same physical vicinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/structurebuilder/capturedstructure(from:))*
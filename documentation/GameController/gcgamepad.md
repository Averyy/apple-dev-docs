# GCGamepad

**Framework**: Game Controller  
**Kind**: class

The standard set of gamepad controls.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCGamepad
```

#### Overview

The controls associated with the gamepad profile include the following:

- Two shoulder buttons.
- Four face buttons arranged in a diamond pattern.
- One directional pad (D-pad).

![None](https://docs-assets.developer.apple.com/published/57237c8130783a4f106842ba76f1ac3b/media-2556316%402x.png)

## Topics

### Determining the Controller That Owns This Profile
- [var controller: GCController?](gcgamepad/controller.md)
  The controller this profile is associated with.
### Determining When Any Element in the Profile Changes
- [var valueChangedHandler: GCGamepadValueChangedHandler?](gcgamepad/valuechangedhandler.md)
  A block called when any element in the profile changes.
### Reading Shoulder Button Inputs
- [var leftShoulder: GCControllerButtonInput](gcgamepad/leftshoulder.md)
  The left shoulder button element.
- [var rightShoulder: GCControllerButtonInput](gcgamepad/rightshoulder.md)
  The right shoulder button element.
### Reading Directional Pad Inputs
- [var dpad: GCControllerDirectionPad](gcgamepad/dpad.md)
  The D-pad element.
### Reading Face Button Inputs
- [var buttonA: GCControllerButtonInput](gcgamepad/buttona.md)
  The bottom face button.
- [var buttonB: GCControllerButtonInput](gcgamepad/buttonb.md)
  The right face button.
- [var buttonX: GCControllerButtonInput](gcgamepad/buttonx.md)
  The left face button.
- [var buttonY: GCControllerButtonInput](gcgamepad/buttony.md)
  The top face button.
### Saving a Snapshot
- [func saveSnapshot() -> GCGamepadSnapshot](gcgamepad/savesnapshot.md)
  Saves a snapshot of all of the profile’s elements.
### Constants
- [typealias GCGamepadValueChangedHandler](gcgamepadvaluechangedhandler.md)
  Signature for the block executed if any element in the gamepad profile changes value.

## Relationships

### Inherits From
- [GCPhysicalInputProfile](gcphysicalinputprofile.md)
### Inherited By
- [GCGamepadSnapshot](gcgamepadsnapshot.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCExtendedGamepadSnapshot](gcextendedgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCExtendedGamepad`](gcextendedgamepad.md) object.
- [class GCGamepadSnapshot](gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](gcgamepad.md) object.
- [class GCMicroGamepadSnapshot](gcmicrogamepadsnapshot.md)
  A recording of all of the values provided by a [`GCMicroGamepad`](gcmicrogamepad.md) object.
- [struct GCExtendedGamepadSnapshotData](gcextendedgamepadsnapshotdata.md)
- [struct GCMicroGamepadSnapshotData](gcmicrogamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](gcextendedgamepadsnapshotdataversion.md)
- [enum GCMicroGamepadSnapshotDataVersion](gcmicrogamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](gcextendedgamepadsnapshotdatafromnsdata(_:_:).md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](gcmicrogamepadsnapshotdatafromnsdata(_:_:).md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](nsdatafromgcextendedgamepadsnapshotdata(_:).md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](nsdatafromgcmicrogamepadsnapshotdata(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepad)*
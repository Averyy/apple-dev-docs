# GCGamepad

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

The standard set of gamepad controls.

**Availability**:
- iOS 7.0+ - Deprecated in 10.0 (renamed: GCExtendedGamepad)
- iPadOS 7.0+ - Deprecated in 10.0 (renamed: GCExtendedGamepad)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: GCExtendedGamepad)
- macOS 10.9+ - Deprecated in 10.12 (renamed: GCExtendedGamepad)
- tvOS 9.0+ - Deprecated in 10.0 (renamed: GCExtendedGamepad)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: GCExtendedGamepad)

## Declaration

```swift
class GCGamepad
```

```objc
@interface GCGamepad : GCPhysicalInputProfile
```

## Overview

The controls associated with the gamepad profile include the following:

- Two shoulder buttons.
- Four face buttons arranged in a diamond pattern.
- One directional pad (D-pad).

![](https://developer.apple.com/tutorials/images/com.apple.gamecontroller/media-2556316@2x.png)

## Topics

### Determining the Controller That Owns This Profile
- [var controller: GCController?](./gcgamepad/controller.md)
  The controller this profile is associated with.
### Determining When Any Element in the Profile Changes
- [var valueChangedHandler: GCGamepadValueChangedHandler?](./gcgamepad/valuechangedhandler.md)
  A block called when any element in the profile changes.
### Reading Shoulder Button Inputs
- [var leftShoulder: GCControllerButtonInput](./gcgamepad/leftshoulder.md)
  The left shoulder button element.
- [var rightShoulder: GCControllerButtonInput](./gcgamepad/rightshoulder.md)
  The right shoulder button element.
### Reading Directional Pad Inputs
- [var dpad: GCControllerDirectionPad](./gcgamepad/dpad.md)
  The D-pad element.
### Reading Face Button Inputs
- [var buttonA: GCControllerButtonInput](./gcgamepad/buttona.md)
  The bottom face button.
- [var buttonB: GCControllerButtonInput](./gcgamepad/buttonb.md)
  The right face button.
- [var buttonX: GCControllerButtonInput](./gcgamepad/buttonx.md)
  The left face button.
- [var buttonY: GCControllerButtonInput](./gcgamepad/buttony.md)
  The top face button.
### Saving a Snapshot
- [func saveSnapshot() -> GCGamepadSnapshot](./gcgamepad/savesnapshot%28%29.md)
  Saves a snapshot of all of the profile’s elements.
### Constants
- [typealias GCGamepadValueChangedHandler](./gcgamepadvaluechangedhandler.md)
  Signature for the block executed if any element in the gamepad profile changes value.

## Relationships

### Inherits From
- [GCPhysicalInputProfile](./gcphysicalinputprofile.md)
### Inherited By
- [GCGamepadSnapshot](./gcgamepadsnapshot.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated symbols
- [class GCExtendedGamepadSnapshot](./gcextendedgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCExtendedGamepad`](./gcextendedgamepad.md) object.
- [class GCGamepadSnapshot](./gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](./gcgamepad.md) object.
- [class GCMicroGamepadSnapshot](./gcmicrogamepadsnapshot.md)
  A recording of all of the values provided by a [`GCMicroGamepad`](./gcmicrogamepad.md) object.
- [struct GCExtendedGamepadSnapshotData](./gcextendedgamepadsnapshotdata.md)
- [struct GCMicroGamepadSnapshotData](./gcmicrogamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](./gcextendedgamepadsnapshotdataversion.md)
- [enum GCMicroGamepadSnapshotDataVersion](./gcmicrogamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](./gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](./gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](./gcextendedgamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](./gcmicrogamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](./nsdatafromgcextendedgamepadsnapshotdata%28_%29.md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](./nsdatafromgcmicrogamepadsnapshotdata%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepad)*
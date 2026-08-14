# UIPointerLockState

**Framework**: UIKit  
**Kind**: class

An object that contains information about a scene’s pointer lock state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPointerLockState
```

#### Overview

To prevent the pointer from triggering system gestures, for example, bringing up the dock, lock it to your application. Locking the pointer hides the pointer and locks it to just your full-screen application.

## Topics

### Checking the Lock State
- [var isLocked: Bool](uipointerlockstate/islocked.md)
  A Boolean value that indicates whether the pointer is locked.
### Updating the Lock State
- [class let didChangeNotification: NSNotification.Name](uipointerlockstate/didchangenotification.md)
  A notification that posts when the value of the locked state for a scene changes.
- [class let sceneUserInfoKey: String](uipointerlockstate/sceneuserinfokey.md)
  A key that reflects the new locked state.
### Structures
- [UIPointerLockState.DidChangeMessage](uipointerlockstate/didchangemessage.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerlockstate)*
# UIHingeInteraction.Update

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An update for a `UIHingeInteraction`

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
class Update
```

```objc
@interface UIHingeInteractionUpdate : NSObject
```

## Topics

### Getting the hinge
- [var hinge: UIHinge?](./update/hinge.md)
  The current hinge state for the interaction, or `nil` when the interaction leaves a hierarchy that provides hinge updates.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihingeinteraction/update)*
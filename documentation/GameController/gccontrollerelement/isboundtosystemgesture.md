# isBoundToSystemGesture

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user binds the element to a system gesture.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isBoundToSystemGesture: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isBoundToSystemGesture) BOOL boundToSystemGesture;
```

#### Discussion

This property is [`true`](../../Swift/true.md) if the user binds this element to a gesture; otherwise, it’s [`false`](../../Swift/false.md).

## See Also

### Handling system gesture input
- [var preferredSystemGestureState: GCControllerElement.SystemGestureState](./preferredsystemgesturestate.md)
  The preferred state for handling input when the user binds the element to a system gesture.
- [GCControllerElement.SystemGestureState](./systemgesturestate.md)
  A state for handling input when an element is part of a system gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/isboundtosystemgesture)*
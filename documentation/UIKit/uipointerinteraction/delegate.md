# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that responds to pointer movements.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIPointerInteractionDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UIPointerInteractionDelegate> delegate;
```

## See Also

### Manage pointer interactions
- [protocol UIPointerInteractionDelegate](../uipointerinteractiondelegate.md)
  An interface for handling pointer movements within the interaction’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteraction/delegate)*
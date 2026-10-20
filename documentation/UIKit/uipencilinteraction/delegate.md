# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that handles the double-tap or squeeze interactions a person makes on Apple Pencil.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+
- visionOS 26.2+

## Declaration

```swift
weak var delegate: (any UIPencilInteractionDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIPencilInteractionDelegate> delegate;
```

## See Also

### Handling interactions
- [protocol UIPencilInteractionDelegate](../uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/delegate)*
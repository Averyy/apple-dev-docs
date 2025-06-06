# delegate

**Framework**: UIKit  
**Kind**: property

The object that handles the double-tap or squeeze interactions a person makes on Apple Pencil.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var delegate: (any UIPencilInteractionDelegate)? { get set }
```

## See Also

- [protocol UIPencilInteractionDelegate](uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/delegate)*
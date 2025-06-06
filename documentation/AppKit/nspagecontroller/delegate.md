# delegate

**Framework**: AppKit  
**Kind**: property

The page controller’s delegate object.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBOutlet
@MainActor weak var delegate: (any NSPageControllerDelegate)? { get set }
```

#### Discussion

The delegate must conform to the [`NSPageControllerDelegate`](nspagecontrollerdelegate.md) protocol.

## See Also

- [protocol NSPageControllerDelegate](nspagecontrollerdelegate.md)
  The `NSPageControllerDelegate` protocol allows you to customize the behavior of instances of the NSPageController class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/delegate)*
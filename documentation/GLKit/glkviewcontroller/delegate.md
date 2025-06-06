# delegate

**Framework**: GLKit  
**Kind**: property

The view controller’s delegate.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var delegate: (any GLKViewControllerDelegate)? { get set }
```

#### Discussion

The delegate is optional.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/delegate)*
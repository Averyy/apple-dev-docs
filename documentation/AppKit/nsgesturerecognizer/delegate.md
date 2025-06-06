# delegate

**Framework**: AppKit  
**Kind**: property

The delegate of the gesture recognizer.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
weak var delegate: (any NSGestureRecognizerDelegate)? { get set }
```

#### Discussion

Use the delegate for fine-grained control over the recognition of a gesture. For example, you can use the delegate to determine whether gesture recognition should begin or whether it should start only after other gesture recognizers fail.

The delegate must implement the [`NSGestureRecognizerDelegate`](nsgesturerecognizerdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/delegate)*
# target

**Framework**: AppKit  
**Kind**: property

The object that implements the action method.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
weak var target: AnyObject? { get set }
```

#### Discussion

The object in this property must implement the method specified by the [`action`](nsgesturerecognizer/action.md) property.

## See Also

- [var action: Selector?](nsgesturerecognizer/action.md)
  The action method to call when the gesture is recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/target)*
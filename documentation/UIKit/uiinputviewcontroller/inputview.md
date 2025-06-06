# inputView

**Framework**: UIKit  
**Kind**: property

The primary view for the input view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var inputView: UIInputView? { get set }
```

#### Discussion

When you use an input view controller subclass as the primary view controller for a custom keyboard, this property’s [`UIInputView`](uiinputview.md) object is initially empty. To display your keyboard’s user interface, add controls and views to the [`inputView`](uiinputviewcontroller/inputview.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/inputview)*
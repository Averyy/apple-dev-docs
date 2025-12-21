# allowsSelfSizing

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the input view is responsible for its own size.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsSelfSizing: Bool { get set }
```

#### Discussion

When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) (the default), UIKit determines an appropriate size of the input view based on its current layout. When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), UIKit honors the value returned by the [`systemLayoutSizeFitting(_:)`](uiview/systemlayoutsizefitting(_:).md) method of the input view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputview/allowsselfsizing)*
# allowsSelfSizing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the input view is responsible for its own size.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allowsSelfSizing: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsSelfSizing;
```

## Discussion

When the value of this property is [`false`](../../Swift/false.md) (the default), UIKit determines an appropriate size of the input view based on its current layout. When the value of this property is [`true`](../../Swift/true.md), UIKit honors the value returned by the [`systemLayoutSizeFitting(_:)`](../uiview/systemlayoutsizefitting%28_%29.md) method of the input view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputview/allowsselfsizing)*
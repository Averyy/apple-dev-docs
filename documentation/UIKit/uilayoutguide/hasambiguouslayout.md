# hasAmbiguousLayout

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the constraints impacting the layout guide specify its location ambiguously.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var hasAmbiguousLayout: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasAmbiguousLayout;
```

## See Also

### Debugging the layout guide
- [func constraintsAffectingLayout(for: NSLayoutConstraint.Axis) -> [NSLayoutConstraint]](./constraintsaffectinglayout%28for%29.md)
  The constraints that impact the layout of the guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide/hasambiguouslayout)*
# constraintsAffectingLayout(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

The constraints that impact the layout of the guide.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func constraintsAffectingLayout(for axis: NSLayoutConstraint.Axis) -> [NSLayoutConstraint]
```

```objc
- (NSArray<__kindof NSLayoutConstraint *> *) constraintsAffectingLayoutForAxis:(UILayoutConstraintAxis) axis;
```

## See Also

### Debugging the layout guide
- [var hasAmbiguousLayout: Bool](./hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the layout guide specify its location ambiguously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguide/constraintsaffectinglayout(for:))*
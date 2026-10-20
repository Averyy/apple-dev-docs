# arrowHeight()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

The height of the arrow (measured in points) from its base to its tip.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+

## Declaration

```swift
static func arrowHeight() -> CGFloat
```

```objc
+ (CGFloat) arrowHeight;
```

#### Discussion

Use this method to return the height of the arrow used by your popover background content. The arrow height must be the same for all possible directions and that height must not change.

## See Also

### Accessing the arrow metrics
- [static func arrowBase() -> CGFloat](./arrowbase%28%29.md)
  The width of the arrow triangle at its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods/arrowheight())*
# contentBleed

**Framework**: TVUIKit  
**Kind**: property

The amount of content that overlaps into the masked portions of the cell.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var contentBleed: UIEdgeInsets { get }
```

#### Discussion

The portions of content that bleed into the masked portions go out of bounds, and consequently disappear from view.

## See Also

- [var cornerRadius: CGFloat](tvcollectionviewfullscreencell/cornerradius.md)
  The radius to use when drawing rounded corners for the cell.
- [var maskAmount: CGFloat](tvcollectionviewfullscreencell/maskamount.md)
  The factor that determines the amount of masking applied on the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell/contentbleed)*
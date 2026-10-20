# contentBleed

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The amount of content that overlaps into the masked portions of the cell.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var contentBleed: UIEdgeInsets { get }
```

```objc
@property (nonatomic, readonly) UIEdgeInsets contentBleed;
```

#### Discussion

The portions of content that bleed into the masked portions go out of bounds, and consequently disappear from view.

## See Also

### Modifying Cell Appearance
- [var cornerRadius: CGFloat](./cornerradius.md)
  The radius to use when drawing rounded corners for the cell.
- [var maskAmount: CGFloat](./maskamount.md)
  The factor that determines the amount of masking applied on the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell/contentbleed)*
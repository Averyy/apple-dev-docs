# cornerRadius

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The radius to use when drawing rounded corners for the cell.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var cornerRadius: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat cornerRadius;
```

#### Discussion

Setting the radius to a value greater than 0.0 points applies increasingly rounded corners to the cell.

## See Also

### Modifying Cell Appearance
- [var contentBleed: UIEdgeInsets](./contentbleed.md)
  The amount of content that overlaps into the masked portions of the cell.
- [var maskAmount: CGFloat](./maskamount.md)
  The factor that determines the amount of masking applied on the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell/cornerradius)*
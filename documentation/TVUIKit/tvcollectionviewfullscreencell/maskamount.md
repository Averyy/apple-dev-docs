# maskAmount

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The factor that determines the amount of masking applied on the cell.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var maskAmount: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat maskAmount;
```

#### Discussion

The amount of masking is determined by attributes of the collection view. A value of 0.0 is applied automatically when the cell is in full screen mode, indicating that there is no masking around the cell. A value of 1.0 is the default masking applied in browsing mode.

## See Also

### Modifying Cell Appearance
- [var contentBleed: UIEdgeInsets](./contentbleed.md)
  The amount of content that overlaps into the masked portions of the cell.
- [var cornerRadius: CGFloat](./cornerradius.md)
  The radius to use when drawing rounded corners for the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell/maskamount)*
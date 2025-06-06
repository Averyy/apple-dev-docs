# maskInset

**Framework**: TVUIKit  
**Kind**: property

The edge insets of the cell mask.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var maskInset: UIEdgeInsets { get set }
```

#### Discussion

Use the `maskInset` property to create a mask around the cell that is only revealed when the cell is brought into focus.

The default value of this property is `UIEdgeInsetsMake(32.0, 120.0, 0.0, 120.0)`.

## See Also

- [var maskAmount: CGFloat](tvcollectionviewfullscreenlayout/maskamount.md)
  The amount by which to mask the cells in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayout/maskinset)*
# maskAmount

**Framework**: TVUIKit  
**Kind**: property

The amount by which to mask the cells in a collection view.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var maskAmount: CGFloat { get set }
```

#### Discussion

Use the `maskAmount` property to change how much masking the collection view applies to its cells. Setting the value of the property on the layout updates the `maskAmount` value of all the cells.

This property can take on a float value between `0` and `1.0`. A value of `0` indicates that the cells are full-screen, and a value of `1.0` indicates that the collection view applies the full mask to its cells.

The default value of this property is `1.0`.

![Diagrams showing a fully masked cell with a maskAmount value of 1.0, and an unmasked cell with a maskAmount value of 0.0.](https://docs-assets.developer.apple.com/published/9069e9947fbc020eab7ea505c4e1e73a/media-4142366%402x.png)

## See Also

- [var maskInset: UIEdgeInsets](tvcollectionviewfullscreenlayout/maskinset.md)
  The edge insets of the cell mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayout/maskamount)*
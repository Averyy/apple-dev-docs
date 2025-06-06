# Changing the appearance of selected and highlighted cells

**Framework**: UIKit

Provide visual feedback to the user about the state of a cell and the transition between states.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Xcode 11.0+

#### Overview

This sample app shows how to change the appearance of collection view cells as they transition between unselected, highlighted, and selected states. As a user taps a cell, the app determines the state of the cell and changes the cell’s appearance to indicate the transition between states.

The collection view in this sample supports single-item selection, which is the default for collection views. You can also configure collection views to support multiple-item selection, or disable selection altogether.

##### Determine the State of a Cell

The collection view in this sample determines the state of a cell by detecting the taps inside its bounds. It then sets the [`isSelected`](uicollectionviewcell/isselected.md) and [`isHighlighted`](uicollectionviewcell/ishighlighted.md) properties of the corresponding cell to indicate the current state. The collection view provides this behavior because its [`allowsSelection`](uicollectionview/allowsselection.md) property is set to `true`.

When touching an unselected cell, the initial touch-down event causes the collection view to change the [`isHighlighted`](uicollectionviewcell/ishighlighted.md) property of the cell to `true`. The final touch-up event causes the highlighted state to return to `false`. If the touch-up event occurs inside the cell, the collection view sets the cell’s [`isSelected`](uicollectionviewcell/isselected.md) property to `true`; otherwise, the property value remains unchanged.

![A diagram depicting the steps that occur when tapping an unselected cell. The first image shows the user's right index finger touching a dark, shaded rectangle representing a collection view cell on a phone screen. Below the image are current property values of the cell, listed as isHighlighted: true and isSelected: false. The second image depicts the user lifting their finger and moving their hand to the right of the rectangle, now shown shaded in a lighter color, on the phone screen. Below, the listed properties isHighlighted and isSelected are both false. The third image depicts the user's hand in the lifted position above the rectangle on the phone screen, with the collection view presenting the rectangle in a third and different shade. Below, the property isHighlighted is false and isSelected is true.](https://docs-assets.developer.apple.com/published/36164f7b9bb80305c20dc4cdff8c5d82/collection-view-selection_2x.png)

##### Change the Cells Visual Appearance

The cell’s [`backgroundView`](uicollectionviewcell/backgroundview.md) property references the view to display as the background of the cell when it loads for the first time and when it isn’t highlighted or selected. When the cell’s state changes to highlighted or selected, the collection view modifies the properties of a cell to indicate the new state. It doesn’t, however, automatically change the visual appearance of the cell. That is, unless you set the cell’s [`selectedBackgroundView`](uicollectionviewcell/selectedbackgroundview.md) property to a view.

Setting the [`selectedBackgroundView`](uicollectionviewcell/selectedbackgroundview.md) to a view causes the collection view to replace the default background with the selected background when highlighting or selecting a cell. Your app doesn’t need to do anything else. The collection view changes the cell’s visual appearance automatically as the cell’s state changes. For example, the sample app uses the [`selectedBackgroundView`](uicollectionviewcell/selectedbackgroundview.md) property to change the cell’s background color from red to blue when selecting the cell.

```swift
override func awakeFromNib() {
    super.awakeFromNib()
    
    let redView = UIView(frame: bounds)
    redView.backgroundColor = #colorLiteral(red: 1, green: 0, blue: 0, alpha: 1)
    self.backgroundView = redView

    let blueView = UIView(frame: bounds)
    blueView.backgroundColor = #colorLiteral(red: 0, green: 0, blue: 1, alpha: 1)
    self.selectedBackgroundView = blueView
}
```

##### Provide Additional Visual Indication of State Changes

Providing a selected background view in a cell is an easy way to have the collection view change the cell’s appearance based on its state, but you can do more than just changing the background. You can, for example, display a checkmark icon in selected cells or distinguish between highlighted and selected states visually.

The collection view’s [`delegate`](uicollectionview/delegate.md) has methods that provide you many opportunities to tweak the selection and highlighting appearance of your collection view. For example, if you prefer to draw the selection state of the cell yourself, you can leave the [`selectedBackgroundView`](uicollectionviewcell/selectedbackgroundview.md) property set to `nil`. Then apply any visual changes to the cell in the [`collectionView(_:didSelectItemAt:)`](uicollectionviewdelegate/collectionview(_:didselectitemat:).md) delegate method. The sample app uses this method, along with the selected background, to show a star in the selected cell. The app removes the star in the [`collectionView(_:didDeselectItemAt:)`](uicollectionviewdelegate/collectionview(_:diddeselectitemat:).md) delegate method.

```swift
func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
    if let cell = collectionView.cellForItem(at: indexPath) as? CustomCollectionViewCell {
        cell.showIcon()
    }
}

func collectionView(_ collectionView: UICollectionView, didDeselectItemAt indexPath: IndexPath) {
    if let cell = collectionView.cellForItem(at: indexPath) as? CustomCollectionViewCell {
        cell.hideIcon()
    }
}
```

If you prefer to draw the highlight state, use the [`collectionView(_:didHighlightItemAt:)`](uicollectionviewdelegate/collectionview(_:didhighlightitemat:).md) and [`collectionView(_:didUnhighlightItemAt:)`](uicollectionviewdelegate/collectionview(_:didunhighlightitemat:).md) delegate methods. The sample app uses these two methods to display a different shade of red as the highlighted background color. Because cells in this app use the blue view for their [`selectedBackgroundView`](uicollectionviewcell/selectedbackgroundview.md), the delegate must apply its changes to the content view of the cells to ensure the changes are visible.

```swift
func collectionView(_ collectionView: UICollectionView, didHighlightItemAt indexPath: IndexPath) {
    if let cell = collectionView.cellForItem(at: indexPath) {
        cell.contentView.backgroundColor = #colorLiteral(red: 1, green: 0.4932718873, blue: 0.4739984274, alpha: 1)
    }
}

func collectionView(_ collectionView: UICollectionView, didUnhighlightItemAt indexPath: IndexPath) {
    if let cell = collectionView.cellForItem(at: indexPath) {
        cell.contentView.backgroundColor = nil
    }
}
```

## See Also

- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/changing-the-appearance-of-selected-and-highlighted-cells)*
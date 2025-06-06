# resolvedColor(with:)

**Framework**: UIKit  
**Kind**: method

Returns the version of the current color that results from the specified traits.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func resolvedColor(with traitCollection: UITraitCollection) -> UIColor
```

#### Return Value

The version of the color to display for the specified traits.

#### Discussion

Use this method when you need to resolve a dynamic color to a specific color value for the specified trait collection. For example, reading the [`cgColor`](uicolor/cgcolor.md) property or calling [`getRed(_:green:blue:alpha:)`](uicolor/getred(_:green:blue:alpha:).md) resolves a dynamic color to a specific color value that’s no longer dynamic. If your calling context isn’t inside one of the methods documented in the [`current`](uitraitcollection/current.md) property, you need to provide a trait collection from an appropriate trait environment, such as your view or view controller.

The example below uses this method set a border color on a [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer):

```swift
// This method sets the border color when UITraitCollection.current is undefined.
func updateBorderColor(layer: CALayer) {
    
    // Read the trait collection from the view.
    let traitCollection = view.traitCollection
    // Use the trait collection to resolve a dynamic color.
    let borderColor = UIColor.label.resolvedColor(with: traitCollection)
    // Use the CGColor value of the resolved color.
    layer.borderColor = borderColor.cgColor
}
```

## Parameters

- `traitCollection`: The traits to use when resolving the color information.

## See Also

- [func performAsCurrent(() -> Void)](uitraitcollection/performascurrent(_:).md)
  Executes custom code using the traits of the receiving trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/resolvedcolor(with:))*
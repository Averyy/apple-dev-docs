# withProminence(_:)

**Framework**: UIKit  
**Kind**: method

Returns the version of the current color that results from applying the specified prominence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func withProminence(_ prominence: UIColor.Prominence) -> UIColor
```

#### Return Value

The version of the color to display for the specified prominence.

#### Discussion

Interface elements, such as text labels, can have a different level of prominence in the UI. For example, a title label appears more prominently than a subtitle or caption. When you specify a label’s color, you can pass one of the [`UIColor.Prominence`](uicolor/prominence-swift.enum.md) constants to [`withProminence(_:)`](uicolor/withprominence(_:).md) to communicate how prominently to display that color in the UI.

The following code creates a label with a secondary, vibrant red color:

```swift
let label = UILabel()
label.preferredVibrancy = .automatic
label.textColor = .systemRed.withProminence(.secondary) 
```

## Parameters

- `prominence`: The prominence to apply to the color. For options, see  .

## See Also

- [var prominence: UIColor.Prominence](uicolor/prominence-swift.property.md)
- [UIColor.Prominence](uicolor/prominence-swift.enum.md)
  A type that indicates the prominence of a color in the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/withprominence(_:))*
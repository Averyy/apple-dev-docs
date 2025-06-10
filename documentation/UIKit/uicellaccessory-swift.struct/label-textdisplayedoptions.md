# label(text:displayed:options:)

**Framework**: UIKit  
**Kind**: method

Creates a label system accessory with the specified text, display state, and configuration options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func label(text: String, displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.LabelOptions = LabelOptions()) -> UICellAccessory
```

#### Return Value

A configured label cell accessory. This accessory appears on the trailing edge of the cell.

#### Discussion

Use this cell accessory to display a short string of text, like a small number showing the count for the associated item.

## Parameters

- `text`: The text for the label to display.
- `displayed`: The cell-editing states that the label accessory appears in. This parameter has a default value of  .
- `options`: Configuration options for the label. See   for possible configuration options.

## See Also

- [UICellAccessory.LabelOptions](uicellaccessory-swift.struct/labeloptions.md)
  Configuration options for a label accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/label(text:displayed:options:))*
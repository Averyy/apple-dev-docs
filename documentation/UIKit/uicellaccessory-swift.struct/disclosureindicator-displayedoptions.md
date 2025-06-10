# disclosureIndicator(displayed:options:)

**Framework**: UIKit  
**Kind**: method

Creates a disclosure indicator system accessory with the specified display state and configuration options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func disclosureIndicator(displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.DisclosureIndicatorOptions = DisclosureIndicatorOptions()) -> UICellAccessory
```

#### Return Value

A configured disclosure indicator cell accessory. This accessory is a disclosure chevron that points in the trailing direction. This accessory appears on the trailing edge of the cell.

#### Discussion

Use this cell accessory to indicate that users can tap on the cell to disclose additional content.

## Parameters

- `displayed`: The cell-editing states that the disclosure indicator appears in. This parameter has a default value of  .
- `options`: Configuration options for the disclosure indicator. See   for possible configuration options.

## See Also

- [UICellAccessory.DisclosureIndicatorOptions](uicellaccessory-swift.struct/disclosureindicatoroptions.md)
  Configuration options for a disclosure indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/disclosureindicator(displayed:options:))*
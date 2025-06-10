# reorder(displayed:options:)

**Framework**: UIKit  
**Kind**: method

Creates a reorder system accessory with the specified display state and configuration options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func reorder(displayed: UICellAccessory.DisplayedState = .whenEditing, options: UICellAccessory.ReorderOptions = ReorderOptions()) -> UICellAccessory
```

#### Return Value

A configured reorder cell accessory. This accessory is three horizontal lines with the default system gray color. This accessory appears on the trailing edge of the cell.

#### Discussion

If your collection view supports interactive reordering of its cells, a user can drag the cell by its reorder accessory to change the order of the cell in the collection view.

## Parameters

- `displayed`: The cell-editing states that the reorder accessory appears in. This parameter has a default value of  .
- `options`: Configuration options for the reorder accessory. See   for possible configuration options.

## See Also

- [UICellAccessory.ReorderOptions](uicellaccessory-swift.struct/reorderoptions.md)
  Configuration options for a reorder accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/reorder(displayed:options:))*
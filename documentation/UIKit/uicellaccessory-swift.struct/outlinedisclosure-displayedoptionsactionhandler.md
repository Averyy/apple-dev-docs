# outlineDisclosure(displayed:options:actionHandler:)

**Framework**: UIKit  
**Kind**: method

Creates an outline disclosure system accessory with the specified display state, configuration options, and optional action handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func outlineDisclosure(displayed: UICellAccessory.DisplayedState = .always, options: UICellAccessory.OutlineDisclosureOptions = OutlineDisclosureOptions(), actionHandler: UICellAccessory.ActionHandler? = nil) -> UICellAccessory
```

#### Return Value

A configured outline disclosure cell accessory. This accessory is a rotating chevron for use in outlines. In iOS and for headers in Mac Catalyst, this accessory appears on the trailing edge. For cells in Mac Catalyst, this accessory appears on the leading edge.

#### Discussion

Use this cell accessory to indicate that an item can expand and collapse, and to enable the user to toggle between the expanded and collapsed states.

## Parameters

- `displayed`: The cell-editing states that the outline disclosure appears in. This parameter has a default value of  .
- `options`: Configuration options for the outline disclosure. See   for possible configuration options.
- `actionHandler`: An optional closure that the system calls when a user interacts with the outline disclosure.

## See Also

- [UICellAccessory.OutlineDisclosureOptions](uicellaccessory-swift.struct/outlinedisclosureoptions.md)
  Configuration options for an outline disclosure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/outlinedisclosure(displayed:options:actionhandler:))*
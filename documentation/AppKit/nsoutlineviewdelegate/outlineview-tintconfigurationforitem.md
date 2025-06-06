# outlineView(_:tintConfigurationForItem:)

**Framework**: AppKit  
**Kind**: method

Customizes an item’s tinting behavior.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, tintConfigurationForItem item: Any) -> NSTintConfiguration?
```

#### Return Value

Returns a new [`NSTintConfiguration`](nstintconfiguration.md) object to create a particular tinting behavior for the item’s row, or `nil` to inherit the tinting behavior from the item’s parent.

#### Discussion

You typically use this method to customize the color for a sidebar.

## Parameters

- `outlineView`: The outline view to which you apply the tinting behavior.
- `item`: The item to which you apply the tinting behavior.

## See Also

- [class NSTintConfiguration](nstintconfiguration.md)
  An object that gives you the ability to choose from system-provided tinting behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:tintconfigurationforitem:))*
# NSPrintPanel.AccessorySummaryKey

**Framework**: AppKit  
**Kind**: struct

Constants that specify the accessory panel keys.

**Availability**:
- macOS ?+

## Declaration

```swift
struct AccessorySummaryKey
```

#### Discussion

These keys must be included in the dictionaries returned by the [`localizedSummaryItems()`](nsprintpanelaccessorizing/localizedsummaryitems().md) method.

## Topics

### Summary Keys
- [static let itemName: NSPrintPanel.AccessorySummaryKey](nsprintpanel/accessorysummarykey/itemname.md)
  A key that specifies the name of the accessory panel setting.
- [static let itemDescription: NSPrintPanel.AccessorySummaryKey](nsprintpanel/accessorysummarykey/itemdescription.md)
  A key that identfies the current value of the accessory panel setting.
### Initializers
- [init(rawValue: String)](nsprintpanel/accessorysummarykey/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func localizedSummaryItems() -> [[NSPrintPanel.AccessorySummaryKey : String]]](nsprintpanelaccessorizing/localizedsummaryitems.md)
  Returns an array of dictionaries containing the localized user setting summary strings.
- [func keyPathsForValuesAffectingPreview() -> Set<String>](nsprintpanelaccessorizing/keypathsforvaluesaffectingpreview.md)
  Returns a set of strings identifying the key paths for any properties that might affect the built-in print preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/accessorysummarykey)*
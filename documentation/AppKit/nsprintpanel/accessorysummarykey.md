# NSPrintPanel.AccessorySummaryKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the accessory panel keys.

**Availability**:
- macOS

## Declaration

```swift
struct AccessorySummaryKey
```

```c
typedef NSString * NSPrintPanelAccessorySummaryKey;
```

## Discussion

These keys must be included in the dictionaries returned by the [`localizedSummaryItems()`](../nsprintpanelaccessorizing/localizedsummaryitems%28%29.md) method.

## Topics

### Summary Keys
- [static let itemName: NSPrintPanel.AccessorySummaryKey](./accessorysummarykey/itemname.md)
  A key that specifies the name of the accessory panel setting.
- [static let itemDescription: NSPrintPanel.AccessorySummaryKey](./accessorysummarykey/itemdescription.md)
  A key that identfies the current value of the accessory panel setting.
### Initializers
- [init(rawValue: String)](./accessorysummarykey/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding to Being Loaded from a Nib File
- [func localizedSummaryItems() -> [[NSPrintPanel.AccessorySummaryKey : String]]](../nsprintpanelaccessorizing/localizedsummaryitems%28%29.md)
  Returns an array of dictionaries containing the localized user setting summary strings.
- [func keyPathsForValuesAffectingPreview() -> Set<String>](../nsprintpanelaccessorizing/keypathsforvaluesaffectingpreview%28%29.md)
  Returns a set of strings identifying the key paths for any properties that might affect the built-in print preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/accessorysummarykey)*
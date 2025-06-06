# NSPrintPanelAccessorizing

**Framework**: AppKit  
**Kind**: protocol

A set of methods that a Print panel object can use to get information from a printing accessory controller.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSPrintPanelAccessorizing
```

#### Overview

A printing accessory controller manages a custom print panel accessory view and is used to coordinate print settings. If you are implementing a custom printing accessory view, your controller must support this protocol. Implementation of only one method in the protocol is actually required. The other method is considered optional and is used to support the print panel’s built-in preview facilities.

## Topics

### Responding to Being Loaded from a Nib File
- [func localizedSummaryItems() -> [[NSPrintPanel.AccessorySummaryKey : String]]](nsprintpanelaccessorizing/localizedsummaryitems.md)
  Returns an array of dictionaries containing the localized user setting summary strings.
- [func keyPathsForValuesAffectingPreview() -> Set<String>](nsprintpanelaccessorizing/keypathsforvaluesaffectingpreview.md)
  Returns a set of strings identifying the key paths for any properties that might affect the built-in print preview.
- [NSPrintPanel.AccessorySummaryKey](nsprintpanel/accessorysummarykey.md)
  Constants that specify the accessory panel keys.

## See Also

- [class NSPDFPanel](nspdfpanel.md)
  A Save or Export as PDF panel that’s consistent with the macOS user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanelaccessorizing)*
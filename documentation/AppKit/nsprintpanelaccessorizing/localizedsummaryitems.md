# localizedSummaryItems()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns an array of dictionaries containing the localized user setting summary strings.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func localizedSummaryItems() -> [[NSPrintPanel.AccessorySummaryKey : String]]
```

#### Return Value

An array of `NSDictionary` objects, each of which contains a `NSPrintPanelAccessorySummaryItemNameKey` and `NSPrintPanelAccessorySummaryItemDescriptionKey` key. The values for the keys are both strings. This method must not return `nil`.

#### Discussion

Accessory panels must implement this method to return information about the panel’s current settings. The returned array should contain a dictionary for each setting that is managed by the accessory panel and each dictionary should contain two key-value pairs identifying the name of the setting and its current value.

Your accessory view must be KVO-compliant for the `localizedSummaryItems` key path because `NSPrintPanel` object observes that key path and uses it to keep the contents of the summary view up to date. This means your view should manually send KVO notifications to observers for the `localizedSummaryItems` key path whenever the contents of the set of summary items changes. For more information on supporting key-value observing and manual notifications, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

- [func keyPathsForValuesAffectingPreview() -> Set<String>](nsprintpanelaccessorizing/keypathsforvaluesaffectingpreview.md)
  Returns a set of strings identifying the key paths for any properties that might affect the built-in print preview.
- [NSPrintPanel.AccessorySummaryKey](nsprintpanel/accessorysummarykey.md)
  Constants that specify the accessory panel keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanelaccessorizing/localizedsummaryitems())*
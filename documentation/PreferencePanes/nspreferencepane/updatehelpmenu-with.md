# updateHelpMenu(with:)

**Framework**: Preference Panes  
**Kind**: method

Updates the help menu.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
func updateHelpMenu(with inArrayOfMenuItems: [[String : String]]?)
```

#### Discussion

Call this method if you need to update help menu items dynamically. If you have static help menu items, you should not use this method. Specify them under the `NSPrefPanelHelpAnchors` key in the bundle’s `Info.plist` instead.

The array contains dictionaries with two keys. Use [`NSPreferencePane`](nspreferencepane.md) for the help menu item title, and [`NSPreferencePane`](nspreferencepane.md) for the anchor reference for `AHLookupAnchor`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/updatehelpmenu(with:))*
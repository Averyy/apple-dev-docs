# shared()

**Framework**: Quick Look UI  
**Kind**: method

Returns the shared Quick Look preview panel instance.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
class func shared() -> QLPreviewPanel!
```

#### Return Value

The shared Quick Look preview panel instance for the application.

#### Discussion

This method creates the panel if it doesn’t exist yet. Use [`sharedPreviewPanelExists()`](qlpreviewpanel/sharedpreviewpanelexists().md) if you want to determine whether the panel exists without creating it.

## See Also

- [class func sharedPreviewPanelExists() -> Bool](qlpreviewpanel/sharedpreviewpanelexists.md)
  Returns a Boolean value that indicates whether the system has created a shared Quick Look preview panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/shared())*
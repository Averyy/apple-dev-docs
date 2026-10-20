# shared()

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Type Method

Returns the shared Quick Look preview panel instance.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func shared() -> QLPreviewPanel!
```

```objc
+ (QLPreviewPanel *) sharedPreviewPanel;
```

#### Return Value

The shared Quick Look preview panel instance for the application.

#### Discussion

This method creates the panel if it doesn’t exist yet. Use [`sharedPreviewPanelExists()`](./sharedpreviewpanelexists%28%29.md) if you want to determine whether the panel exists without creating it.

## See Also

### Accessing the Shared Panel
- [class func sharedPreviewPanelExists() -> Bool](./sharedpreviewpanelexists%28%29.md)
  Returns a Boolean value that indicates whether the system has created a shared Quick Look preview panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/shared())*
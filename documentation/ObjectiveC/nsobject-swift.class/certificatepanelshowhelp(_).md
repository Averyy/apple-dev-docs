# certificatePanelShowHelp(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Implements custom help behavior for the modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func certificatePanelShowHelp(_ sender: SFCertificatePanel!) -> Bool
```

```objc
- (BOOL) certificatePanelShowHelp:(SFCertificatePanel *) sender;
```

## Discussion

You can use this delegate method to implement custom help if you call the [`setShowsHelp(_:)`](../../SecurityInterface/sfcertificatepanel/setshowshelp%28_%29.md) method to display a help button in the sheet or panel. If you are not implementing custom help, do not implement this method.

## Parameters

- `sender`: The certificate panel for which to implement custom help.

## See Also

### Related Documentation
- [var delegate: (any NSWindowDelegate)?](../../AppKit/nswindow/delegate.md)
  The window’s delegate.
- [func setShowsHelp(Bool)](../../SecurityInterface/sfcertificatepanel/setshowshelp%28_%29.md)
  Displays a Help button in the sheet or panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/certificatepanelshowhelp(_:))*
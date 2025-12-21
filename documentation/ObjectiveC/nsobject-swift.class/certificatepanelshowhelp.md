# certificatePanelShowHelp(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Implements custom help behavior for the modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func certificatePanelShowHelp(_ sender: SFCertificatePanel!) -> Bool
```

#### Discussion

You can use this delegate method to implement custom help if you call the [`setShowsHelp(_:)`](https://developer.apple.com/documentation/SecurityInterface/SFCertificatePanel/setShowsHelp(_:)) method to display a help button in the sheet or panel. If you are not implementing custom help, do not implement this method.

## Parameters

- `sender`: The certificate panel for which to implement custom help.

## See Also

- [var delegate: (any NSWindowDelegate)?](../AppKit/NSWindow/delegate.md)
  The window’s delegate.
- [@MainActor func setShowsHelp(_ showsHelp: Bool)](../SecurityInterface/SFCertificatePanel/setShowsHelp(_:).md)
  Displays a Help button in the sheet or panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/certificatepanelshowhelp(_:))*
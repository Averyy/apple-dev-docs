# takeSettings(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the print info with all the settings and attributes in the specified PDF info object.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func takeSettings(from inPDFInfo: NSPDFInfo)
```

```objc
- (void) takeSettingsFromPDFInfo:(NSPDFInfo *) inPDFInfo;
```

## See Also

### Accessing Core Printing Information
- [var printSettings: NSMutableDictionary](./printsettings.md)
  A mutable dictionary containing the print settings from Core Printing.
- [NSPrintInfo.SettingKey](./settingkey.md)
  The type you use to specify a print info setting key.
- [func pmPrintSession() -> UnsafeMutableRawPointer](./pmprintsession%28%29.md)
  Returns a Core Printing object configured with the print info’s session information.
- [func pmPageFormat() -> UnsafeMutableRawPointer](./pmpageformat%28%29.md)
  Returns a Core Printing object configured with the print info’s page format information.
- [func pmPrintSettings() -> UnsafeMutableRawPointer](./pmprintsettings%28%29.md)
  Returns a Core Printing object configured with the print info’s print settings information
- [func updateFromPMPageFormat()](./updatefrompmpageformat%28%29.md)
  Synchronizes the print info’s page format information with information from its associated page format object.
- [func updateFromPMPrintSettings()](./updatefrompmprintsettings%28%29.md)
  Synchronizes the print info’s print settings information with information from its associated print settings object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/takesettings(from:))*
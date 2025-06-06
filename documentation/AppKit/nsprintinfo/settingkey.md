# NSPrintInfo.SettingKey

**Framework**: AppKit  
**Kind**: typealias

The type you use to specify a print info setting key.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias SettingKey = String
```

## See Also

- [var printSettings: NSMutableDictionary](nsprintinfo/printsettings.md)
  A mutable dictionary containing the print settings from Core Printing.
- [func pmPrintSession() -> UnsafeMutableRawPointer](nsprintinfo/pmprintsession.md)
  Returns a Core Printing object configured with the print info’s session information.
- [func pmPageFormat() -> UnsafeMutableRawPointer](nsprintinfo/pmpageformat.md)
  Returns a Core Printing object configured with the print info’s page format information.
- [func pmPrintSettings() -> UnsafeMutableRawPointer](nsprintinfo/pmprintsettings.md)
  Returns a Core Printing object configured with the print info’s print settings information
- [func updateFromPMPageFormat()](nsprintinfo/updatefrompmpageformat.md)
  Synchronizes the print info’s page format information with information from its associated page format object.
- [func updateFromPMPrintSettings()](nsprintinfo/updatefrompmprintsettings.md)
  Synchronizes the print info’s print settings information with information from its associated print settings object.
- [func takeSettings(from: NSPDFInfo)](nsprintinfo/takesettings(from:).md)
  Updates the print info with all the settings and attributes in the specified PDF info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/settingkey)*
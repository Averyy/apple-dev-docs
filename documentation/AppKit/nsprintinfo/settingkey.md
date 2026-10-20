# NSPrintInfo.SettingKey

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

The type you use to specify a print info setting key.

**Availability**:
- macOS

## Declaration

```swift
typealias SettingKey = String
```

```c
typedef NSString * NSPrintInfoSettingKey;
```

## See Also

### Accessing Core Printing Information
- [var printSettings: NSMutableDictionary](./printsettings.md)
  A mutable dictionary containing the print settings from Core Printing.
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
- [func takeSettings(from: NSPDFInfo)](./takesettings%28from%29.md)
  Updates the print info with all the settings and attributes in the specified PDF info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/settingkey)*
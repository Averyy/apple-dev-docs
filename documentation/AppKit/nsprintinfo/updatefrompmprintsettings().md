# updateFromPMPrintSettings()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Synchronizes the print info’s print settings information with information from its associated print settings object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func updateFromPMPrintSettings()
```

```objc
- (void) updateFromPMPrintSettings;
```

## Discussion

You should use this method after making changes to the `PMPrintSettings` object obtained from the receiver. Each `NSPrintInfo` object keeps track of the object returned from its [`pmPrintSettings()`](./pmprintsettings%28%29.md) method and obtains any updated information from the object directly. You only need to synchronize the objects once when you have made all of the desired changes.

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
- [func takeSettings(from: NSPDFInfo)](./takesettings%28from%29.md)
  Updates the print info with all the settings and attributes in the specified PDF info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/updatefrompmprintsettings())*
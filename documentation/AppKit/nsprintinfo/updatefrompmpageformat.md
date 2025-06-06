# updateFromPMPageFormat()

**Framework**: AppKit  
**Kind**: method

Synchronizes the print info’s page format information with information from its associated page format object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func updateFromPMPageFormat()
```

#### Discussion

You should use this method after making changes to the `PMPageFormat` object obtained from the receiver. Each `NSPrintInfo` object keeps track of the object returned from its [`pmPageFormat()`](nsprintinfo/pmpageformat().md) method and obtains any updated information from the object directly. You only need to synchronize the objects once when you have made all of the desired changes.

## See Also

- [var printSettings: NSMutableDictionary](nsprintinfo/printsettings.md)
  A mutable dictionary containing the print settings from Core Printing.
- [NSPrintInfo.SettingKey](nsprintinfo/settingkey.md)
  The type you use to specify a print info setting key.
- [func pmPrintSession() -> UnsafeMutableRawPointer](nsprintinfo/pmprintsession.md)
  Returns a Core Printing object configured with the print info’s session information.
- [func pmPageFormat() -> UnsafeMutableRawPointer](nsprintinfo/pmpageformat.md)
  Returns a Core Printing object configured with the print info’s page format information.
- [func pmPrintSettings() -> UnsafeMutableRawPointer](nsprintinfo/pmprintsettings.md)
  Returns a Core Printing object configured with the print info’s print settings information
- [func updateFromPMPrintSettings()](nsprintinfo/updatefrompmprintsettings.md)
  Synchronizes the print info’s print settings information with information from its associated print settings object.
- [func takeSettings(from: NSPDFInfo)](nsprintinfo/takesettings(from:).md)
  Updates the print info with all the settings and attributes in the specified PDF info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/updatefrompmpageformat())*
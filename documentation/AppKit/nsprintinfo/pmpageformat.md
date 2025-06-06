# pmPageFormat()

**Framework**: AppKit  
**Kind**: method

Returns a Core Printing object configured with the print info’s page format information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func pmPageFormat() -> UnsafeMutableRawPointer
```

#### Return Value

A pointer to a [`PMPageFormat`](https://developer.apple.com/documentation/applicationservices/pmpageformat) object, an opaque data type that stores information such as the paper size, orientation, and scale of pages in a printing session. You should not call `PMRelease` to release the returned object, except to balance calls to `PMRetain` that your code also issued.

#### Discussion

The information in the returned `PMPageFormat` object is consistent with the receiver’s page format information at the time this method is called. Subsequent changes to the receiving `NSPrintInfo` object do not result in changes to the information in the `PMPageFormat` object.

If you make changes to the data in the `PMPageFormat` object, you should invoke the [`updateFromPMPageFormat()`](nsprintinfo/updatefrompmpageformat().md) method to synchronize those changes with the `NSPrintInfo` object that created the object.

## See Also

- [var printSettings: NSMutableDictionary](nsprintinfo/printsettings.md)
  A mutable dictionary containing the print settings from Core Printing.
- [NSPrintInfo.SettingKey](nsprintinfo/settingkey.md)
  The type you use to specify a print info setting key.
- [func pmPrintSession() -> UnsafeMutableRawPointer](nsprintinfo/pmprintsession.md)
  Returns a Core Printing object configured with the print info’s session information.
- [func pmPrintSettings() -> UnsafeMutableRawPointer](nsprintinfo/pmprintsettings.md)
  Returns a Core Printing object configured with the print info’s print settings information
- [func updateFromPMPageFormat()](nsprintinfo/updatefrompmpageformat.md)
  Synchronizes the print info’s page format information with information from its associated page format object.
- [func updateFromPMPrintSettings()](nsprintinfo/updatefrompmprintsettings.md)
  Synchronizes the print info’s print settings information with information from its associated print settings object.
- [func takeSettings(from: NSPDFInfo)](nsprintinfo/takesettings(from:).md)
  Updates the print info with all the settings and attributes in the specified PDF info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/pmpageformat())*
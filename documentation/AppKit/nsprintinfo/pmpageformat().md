# pmPageFormat()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Core Printing object configured with the print info’s page format information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func pmPageFormat() -> UnsafeMutableRawPointer
```

```objc
- (void *) PMPageFormat;
```

## Return Value

A pointer to a [`PMPageFormat`](../../applicationservices/pmpageformat.md) object, an opaque data type that stores information such as the paper size, orientation, and scale of pages in a printing session. You should not call `PMRelease` to release the returned object, except to balance calls to `PMRetain` that your code also issued.

## Discussion

The information in the returned `PMPageFormat` object is consistent with the receiver’s page format information at the time this method is called. Subsequent changes to the receiving `NSPrintInfo` object do not result in changes to the information in the `PMPageFormat` object.

If you make changes to the data in the `PMPageFormat` object, you should invoke the [`updateFromPMPageFormat()`](./updatefrompmpageformat%28%29.md) method to synchronize those changes with the `NSPrintInfo` object that created the object.

## See Also

### Accessing Core Printing Information
- [var printSettings: NSMutableDictionary](./printsettings.md)
  A mutable dictionary containing the print settings from Core Printing.
- [NSPrintInfo.SettingKey](./settingkey.md)
  The type you use to specify a print info setting key.
- [func pmPrintSession() -> UnsafeMutableRawPointer](./pmprintsession%28%29.md)
  Returns a Core Printing object configured with the print info’s session information.
- [func pmPrintSettings() -> UnsafeMutableRawPointer](./pmprintsettings%28%29.md)
  Returns a Core Printing object configured with the print info’s print settings information
- [func updateFromPMPageFormat()](./updatefrompmpageformat%28%29.md)
  Synchronizes the print info’s page format information with information from its associated page format object.
- [func updateFromPMPrintSettings()](./updatefrompmprintsettings%28%29.md)
  Synchronizes the print info’s print settings information with information from its associated print settings object.
- [func takeSettings(from: NSPDFInfo)](./takesettings%28from%29.md)
  Updates the print info with all the settings and attributes in the specified PDF info object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/pmpageformat())*
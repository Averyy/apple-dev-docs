# CTFontManagerError.unsupportedScope

**Framework**: Core Text  
**Kind**: case  
**Role**: Case

An error that indicates the specified scope isn’t supported.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case unsupportedScope
```

```c
kCTFontManagerErrorUnsupportedScope
```

## See Also

### Constants
- [CTFontManagerError.fileNotFound](./filenotfound.md)
  An error that indicates the file doesn’t exist at the specified URL.
- [CTFontManagerError.insufficientPermissions](./insufficientpermissions.md)
  An error that indicates insufficient permissions to access the file.
- [CTFontManagerError.unrecognizedFormat](./unrecognizedformat.md)
  An error that indicates the file’s format is unrecognized or unsupported.
- [CTFontManagerError.invalidFontData](./invalidfontdata.md)
  An error that indicates the file contains invalid font data that could cause system problems.
- [CTFontManagerError.alreadyRegistered](./alreadyregistered.md)
  An error that indicates the file is already registered in the specified scope.
- [CTFontManagerError.exceededResourceLimit](./exceededresourcelimit.md)
  An error that indicates an operation failure due to a system limitation.
- [CTFontManagerError.assetNotFound](./assetnotfound.md)
  An error that indicates the asset isn’t found.
- [CTFontManagerError.notRegistered](./notregistered.md)
  An error that indicates the file isn’t registered in the specified scope.
- [CTFontManagerError.inUse](./inuse.md)
  An error that indicates the font file is actively in use and can’t be unregistered.
- [CTFontManagerError.systemRequired](./systemrequired.md)
  An error that indicates the file is required by the system and can’t be unregistered.
- [CTFontManagerError.registrationFailed](./registrationfailed.md)
  An error that indicates the file can’t be processed due to an unexpected FontProvider error.
- [CTFontManagerError.missingEntitlement](./missingentitlement.md)
  An error that indicates the file can’t be processed because the provider doesn’t have a necessary entitlement.
- [CTFontManagerError.insufficientInfo](./insufficientinfo.md)
  An error that indicates the font descriptor doesn’t have the necessary information to specify a font file.
- [CTFontManagerError.cancelledByUser](./cancelledbyuser.md)
  An error that indicates the user cancelled the operation.
- [CTFontManagerError.duplicatedName](./duplicatedname.md)
  An error that indicates the file can’t register because of a duplicate font name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagererror/unsupportedscope)*
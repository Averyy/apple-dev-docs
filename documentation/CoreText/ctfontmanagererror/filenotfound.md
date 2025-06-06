# CTFontManagerError.fileNotFound

**Framework**: Core Text  
**Kind**: case

An error that indicates the file doesn’t exist at the specified URL.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case fileNotFound
```

## See Also

- [CTFontManagerError.insufficientPermissions](ctfontmanagererror/insufficientpermissions.md)
  An error that indicates insufficient permissions to access the file.
- [CTFontManagerError.unrecognizedFormat](ctfontmanagererror/unrecognizedformat.md)
  An error that indicates the file’s format is unrecognized or unsupported.
- [CTFontManagerError.invalidFontData](ctfontmanagererror/invalidfontdata.md)
  An error that indicates the file contains invalid font data that could cause system problems.
- [CTFontManagerError.alreadyRegistered](ctfontmanagererror/alreadyregistered.md)
  An error that indicates the file is already registered in the specified scope.
- [CTFontManagerError.exceededResourceLimit](ctfontmanagererror/exceededresourcelimit.md)
  An error that indicates an operation failure due to a system limitation.
- [CTFontManagerError.assetNotFound](ctfontmanagererror/assetnotfound.md)
  An error that indicates the asset isn’t found.
- [CTFontManagerError.notRegistered](ctfontmanagererror/notregistered.md)
  An error that indicates the file isn’t registered in the specified scope.
- [CTFontManagerError.inUse](ctfontmanagererror/inuse.md)
  An error that indicates the font file is actively in use and can’t be unregistered.
- [CTFontManagerError.systemRequired](ctfontmanagererror/systemrequired.md)
  An error that indicates the file is required by the system and can’t be unregistered.
- [CTFontManagerError.registrationFailed](ctfontmanagererror/registrationfailed.md)
  An error that indicates the file can’t be processed due to an unexpected FontProvider error.
- [CTFontManagerError.missingEntitlement](ctfontmanagererror/missingentitlement.md)
  An error that indicates the file can’t be processed because the provider doesn’t have a necessary entitlement.
- [CTFontManagerError.insufficientInfo](ctfontmanagererror/insufficientinfo.md)
  An error that indicates the font descriptor doesn’t have the necessary information to specify a font file.
- [CTFontManagerError.cancelledByUser](ctfontmanagererror/cancelledbyuser.md)
  An error that indicates the user cancelled the operation.
- [CTFontManagerError.duplicatedName](ctfontmanagererror/duplicatedname.md)
  An error that indicates the file can’t register because of a duplicate font name.
- [CTFontManagerError.invalidFilePath](ctfontmanagererror/invalidfilepath.md)
  An error that indicates the file isn’t in an allowed location, which must be either in the app’s bundle or an on-demand resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagererror/filenotfound)*
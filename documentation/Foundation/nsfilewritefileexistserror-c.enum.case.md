# NSFileWriteFileExistsError

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

Could not perform an operation because the destination file already exists.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
NSFileWriteFileExistsError
```

## Discussion

This error can be produced by the [`FileManager`](./filemanager.md) class’s copy, move, and link methods

## See Also

### Error Codes
- [NSFileNoSuchFileError](./nsfilenosuchfileerror-c.enum.case.md)
  A filesystem operation was attempted on a non-existent file.
- [NSFileLockingError](./nsfilelockingerror-c.enum.case.md)
  The file could not be locked.
- [NSFileReadUnknownError](./nsfilereadunknownerror-c.enum.case.md)
  Could not read, for unknown reasons.
- [NSFileReadNoPermissionError](./nsfilereadnopermissionerror-c.enum.case.md)
  Could not read because of a permission problem.
- [NSFileReadInvalidFileNameError](./nsfilereadinvalidfilenameerror-c.enum.case.md)
  Could not read because of an invalid file name.
- [NSFileReadCorruptFileError](./nsfilereadcorruptfileerror-c.enum.case.md)
  Could not read because of a corrupted file, bad format, or similar reason.
- [NSFileReadNoSuchFileError](./nsfilereadnosuchfileerror-c.enum.case.md)
  Could not read because no such file was found.
- [NSFileReadInapplicableStringEncodingError](./nsfilereadinapplicablestringencodingerror-c.enum.case.md)
  Could not read because the string encoding wasn’t applicable.
- [NSFileReadUnsupportedSchemeError](./nsfilereadunsupportedschemeerror-c.enum.case.md)
  Could not read because the specified URL scheme is unsupported.
- [NSFileReadTooLargeError](./nsfilereadtoolargeerror-c.enum.case.md)
  Could not read because the specified file was too large.
- [NSFileReadUnknownStringEncodingError](./nsfilereadunknownstringencodingerror-c.enum.case.md)
  Could not read because the string coding of the file couldn’t be determined.
- [NSFileWriteUnknownError](./nsfilewriteunknownerror-c.enum.case.md)
  Could not write, for unknown reasons.
- [NSFileWriteNoPermissionError](./nsfilewritenopermissionerror-c.enum.case.md)
  Could not write because of a permission problem.
- [NSFileWriteInvalidFileNameError](./nsfilewriteinvalidfilenameerror-c.enum.case.md)
  Could not write because of an invalid file name.
- [NSFileWriteInapplicableStringEncodingError](./nsfilewriteinapplicablestringencodingerror-c.enum.case.md)
  Could not write because the string encoding was not applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilewritefileexistserror-c.enum.case)*
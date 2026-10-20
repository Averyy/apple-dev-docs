# NSFileWriteFileExistsError

**Framework**: Foundation  
**Kind**: var

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

```swift
var NSFileWriteFileExistsError: Int { get }
```

#### Discussion

This error can be produced by the [`FileManager`](filemanager.md) class’s copy, move, and link methods

## See Also

- [var NSFileNoSuchFileError: Int](nsfilenosuchfileerror-swift.var.md)
  A filesystem operation was attempted on a non-existent file.
- [var NSFileLockingError: Int](nsfilelockingerror-swift.var.md)
  The file could not be locked.
- [var NSFileReadUnknownError: Int](nsfilereadunknownerror-swift.var.md)
  Could not read, for unknown reasons.
- [var NSFileReadNoPermissionError: Int](nsfilereadnopermissionerror-swift.var.md)
  Could not read because of a permission problem.
- [var NSFileReadInvalidFileNameError: Int](nsfilereadinvalidfilenameerror-swift.var.md)
  Could not read because of an invalid file name.
- [var NSFileReadCorruptFileError: Int](nsfilereadcorruptfileerror-swift.var.md)
  Could not read because of a corrupted file, bad format, or similar reason.
- [var NSFileReadNoSuchFileError: Int](nsfilereadnosuchfileerror-swift.var.md)
  Could not read because no such file was found.
- [var NSFileReadInapplicableStringEncodingError: Int](nsfilereadinapplicablestringencodingerror-swift.var.md)
  Could not read because the string encoding wasn’t applicable.
- [var NSFileReadUnsupportedSchemeError: Int](nsfilereadunsupportedschemeerror-swift.var.md)
  Could not read because the specified URL scheme is unsupported.
- [var NSFileReadTooLargeError: Int](nsfilereadtoolargeerror-swift.var.md)
  Could not read because the specified file was too large.
- [var NSFileReadUnknownStringEncodingError: Int](nsfilereadunknownstringencodingerror-swift.var.md)
  Could not read because the string coding of the file couldn’t be determined.
- [var NSFileWriteUnknownError: Int](nsfilewriteunknownerror-swift.var.md)
  Could not write, for unknown reasons.
- [var NSFileWriteNoPermissionError: Int](nsfilewritenopermissionerror-swift.var.md)
  Could not write because of a permission problem.
- [var NSFileWriteInvalidFileNameError: Int](nsfilewriteinvalidfilenameerror-swift.var.md)
  Could not write because of an invalid file name.
- [var NSFileWriteInapplicableStringEncodingError: Int](nsfilewriteinapplicablestringencodingerror-swift.var.md)
  Could not write because the string encoding was not applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilewritefileexistserror-swift.var)*
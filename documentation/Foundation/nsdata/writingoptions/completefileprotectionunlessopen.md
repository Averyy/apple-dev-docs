# completeFileProtectionUnlessOpen

**Framework**: Foundation  
**Kind**: property

An option to allow the file to be accessible while the device is unlocked or the file is already open.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var completeFileProtectionUnlessOpen: NSData.WritingOptions { get }
```

#### Discussion

In this case, your app cannot open the file to read it or write to it when the device is locked, but your app can create new files with this class. If one of these files is open when the device is locked, your app can read and write to the opened file.

## See Also

- [static var atomic: NSData.WritingOptions](nsdata/writingoptions/atomic.md)
  An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [static var withoutOverwriting: NSData.WritingOptions](nsdata/writingoptions/withoutoverwriting.md)
  An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [static var noFileProtection: NSData.WritingOptions](nsdata/writingoptions/nofileprotection.md)
  An option to not encrypt the file when writing it out.
- [static var completeFileProtection: NSData.WritingOptions](nsdata/writingoptions/completefileprotection.md)
  An option to make the file accessible only while the device is unlocked.
- [static var completeFileProtectionUntilFirstUserAuthentication: NSData.WritingOptions](nsdata/writingoptions/completefileprotectionuntilfirstuserauthentication.md)
  An option to allow the file to be accessible after a user first unlocks the device.
- [static var fileProtectionMask: NSData.WritingOptions](nsdata/writingoptions/fileprotectionmask.md)
  An option the system uses when determining the file protection options that the system assigns to the data.
- [static var atomic: NSData.WritingOptions](nsdata/writingoptions/atomic.md)
  An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [static var withoutOverwriting: NSData.WritingOptions](nsdata/writingoptions/withoutoverwriting.md)
  An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [static var noFileProtection: NSData.WritingOptions](nsdata/writingoptions/nofileprotection.md)
  An option to not encrypt the file when writing it out.
- [static var completeFileProtection: NSData.WritingOptions](nsdata/writingoptions/completefileprotection.md)
  An option to make the file accessible only while the device is unlocked.
- [static var completeFileProtectionUntilFirstUserAuthentication: NSData.WritingOptions](nsdata/writingoptions/completefileprotectionuntilfirstuserauthentication.md)
  An option to allow the file to be accessible after a user first unlocks the device.
- [static var fileProtectionMask: NSData.WritingOptions](nsdata/writingoptions/fileprotectionmask.md)
  An option the system uses when determining the file protection options that the system assigns to the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/writingoptions/completefileprotectionunlessopen)*
# completeFileProtection

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An option to make the file accessible only while the device is unlocked.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var completeFileProtection: NSData.WritingOptions { get }
```

```c
NSDataWritingFileProtectionComplete
```

#### Discussion

In this case, the system stores the file in an encrypted format and your app may only read or write to the file while the device is unlocked. At all other times, any  attempts your app makes to read and write the file will fail.

## See Also

### Constants
- [static var atomic: NSData.WritingOptions](./atomic.md)
  An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [static var withoutOverwriting: NSData.WritingOptions](./withoutoverwriting.md)
  An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [static var noFileProtection: NSData.WritingOptions](./nofileprotection.md)
  An option to not encrypt the file when writing it out.
- [static var completeFileProtectionUnlessOpen: NSData.WritingOptions](./completefileprotectionunlessopen.md)
  An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [static var completeFileProtectionUntilFirstUserAuthentication: NSData.WritingOptions](./completefileprotectionuntilfirstuserauthentication.md)
  An option to allow the file to be accessible after a user first unlocks the device.
- [static var fileProtectionMask: NSData.WritingOptions](./fileprotectionmask.md)
  An option the system uses when determining the file protection options that the system assigns to the data.
- [static var completeFileProtectionWhenUserInactive: NSData.WritingOptions](./completefileprotectionwhenuserinactive.md)
  An option to allow the file to be accessible after a user first unlocks the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/writingoptions/completefileprotection)*
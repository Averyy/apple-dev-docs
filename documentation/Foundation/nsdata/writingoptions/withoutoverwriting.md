# withoutOverwriting

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An option that attempts to write data to a file and fails with an error if the destination file already exists.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var withoutOverwriting: NSData.WritingOptions { get }
```

```c
NSDataWritingWithoutOverwriting
```

#### Discussion

You can’t combine this constant with [`atomic`](./atomic.md) because atomic allows the system to overwrite the original file.

## See Also

### Constants
- [static var atomic: NSData.WritingOptions](./atomic.md)
  An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [static var noFileProtection: NSData.WritingOptions](./nofileprotection.md)
  An option to not encrypt the file when writing it out.
- [static var completeFileProtection: NSData.WritingOptions](./completefileprotection.md)
  An option to make the file accessible only while the device is unlocked.
- [static var completeFileProtectionUnlessOpen: NSData.WritingOptions](./completefileprotectionunlessopen.md)
  An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [static var completeFileProtectionUntilFirstUserAuthentication: NSData.WritingOptions](./completefileprotectionuntilfirstuserauthentication.md)
  An option to allow the file to be accessible after a user first unlocks the device.
- [static var fileProtectionMask: NSData.WritingOptions](./fileprotectionmask.md)
  An option the system uses when determining the file protection options that the system assigns to the data.
- [static var completeFileProtectionWhenUserInactive: NSData.WritingOptions](./completefileprotectionwhenuserinactive.md)
  An option to allow the file to be accessible after a user first unlocks the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/writingoptions/withoutoverwriting)*
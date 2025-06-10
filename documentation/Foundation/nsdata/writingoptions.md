# NSData.WritingOptions

**Framework**: Foundation  
**Kind**: struct

Options for methods used to write data objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct WritingOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](nsdata/writingoptions/init(rawvalue:).md)
### Constants
- [static var atomic: NSData.WritingOptions](nsdata/writingoptions/atomic.md)
  An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [static var withoutOverwriting: NSData.WritingOptions](nsdata/writingoptions/withoutoverwriting.md)
  An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [static var noFileProtection: NSData.WritingOptions](nsdata/writingoptions/nofileprotection.md)
  An option to not encrypt the file when writing it out.
- [static var completeFileProtection: NSData.WritingOptions](nsdata/writingoptions/completefileprotection.md)
  An option to make the file accessible only while the device is unlocked.
- [static var completeFileProtectionUnlessOpen: NSData.WritingOptions](nsdata/writingoptions/completefileprotectionunlessopen.md)
  An option to allow the file to be accessible while the device is unlocked or the file is already open.
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
- [static var completeFileProtectionUnlessOpen: NSData.WritingOptions](nsdata/writingoptions/completefileprotectionunlessopen.md)
  An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [static var completeFileProtectionUntilFirstUserAuthentication: NSData.WritingOptions](nsdata/writingoptions/completefileprotectionuntilfirstuserauthentication.md)
  An option to allow the file to be accessible after a user first unlocks the device.
- [static var fileProtectionMask: NSData.WritingOptions](nsdata/writingoptions/fileprotectionmask.md)
  An option the system uses when determining the file protection options that the system assigns to the data.
### Legacy Constants
- [static var atomicWrite: NSData.WritingOptions](nsdata/writingoptions/atomicwrite.md)
  An option that attempts to write data to an auxiliary file first and then exchange the files.
- [static var atomicWrite: NSData.WritingOptions](nsdata/writingoptions/atomicwrite.md)
  An option that attempts to write data to an auxiliary file first and then exchange the files.
### Entitlements
- [Data Protection Entitlement](../BundleResources/Entitlements/com.apple.developer.default-data-protection.md)
  The level of data protection for sensitive user data when an app accesses it on a device.
### Type Properties
- [static var completeFileProtectionWhenUserInactive: NSData.WritingOptions](nsdata/writingoptions/completefileprotectionwhenuserinactive.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func write(toFile: String, atomically: Bool) -> Bool](nsdata/write(tofile:atomically:).md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(toFile: String, options: NSData.WritingOptions) throws](nsdata/write(tofile:options:).md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](nsdata/write(to:atomically:).md)
  Writes the data object’s bytes to the location specified by a given URL.
- [func write(to: URL, options: NSData.WritingOptions) throws](nsdata/write(to:options:).md)
  Writes the data object’s bytes to the location specified by a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/writingoptions)*
# NSData.WritingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSDataWritingOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./writingoptions/init%28rawvalue%29.md)
### Constants
- [static var atomic: NSData.WritingOptions](./writingoptions/atomic.md)
  An option to write data to an auxiliary file first and then replace the original file with the auxiliary file when the write completes.
- [static var withoutOverwriting: NSData.WritingOptions](./writingoptions/withoutoverwriting.md)
  An option that attempts to write data to a file and fails with an error if the destination file already exists.
- [static var noFileProtection: NSData.WritingOptions](./writingoptions/nofileprotection.md)
  An option to not encrypt the file when writing it out.
- [static var completeFileProtection: NSData.WritingOptions](./writingoptions/completefileprotection.md)
  An option to make the file accessible only while the device is unlocked.
- [static var completeFileProtectionUnlessOpen: NSData.WritingOptions](./writingoptions/completefileprotectionunlessopen.md)
  An option to allow the file to be accessible while the device is unlocked or the file is already open.
- [static var completeFileProtectionUntilFirstUserAuthentication: NSData.WritingOptions](./writingoptions/completefileprotectionuntilfirstuserauthentication.md)
  An option to allow the file to be accessible after a user first unlocks the device.
- [static var fileProtectionMask: NSData.WritingOptions](./writingoptions/fileprotectionmask.md)
  An option the system uses when determining the file protection options that the system assigns to the data.
- [static var completeFileProtectionWhenUserInactive: NSData.WritingOptions](./writingoptions/completefileprotectionwhenuserinactive.md)
  An option to allow the file to be accessible after a user first unlocks the device.
### Legacy Constants
- [static var atomicWrite: NSData.WritingOptions](./writingoptions/atomicwrite.md)
  An option that attempts to write data to an auxiliary file first and then exchange the files.
- [static var atomicWrite: NSData.WritingOptions](./writingoptions/atomicwrite.md)
  An option that attempts to write data to an auxiliary file first and then exchange the files.
### Entitlements
- [Data Protection Entitlement](../../BundleResources/entitlements/com.apple.developer.default-data-protection.md)
  The level of data protection for sensitive user data when an app accesses it on a device.
### Instance Methods
- [func contains(Data.WritingOptions) -> Bool](./writingoptions/contains%28_%29.md)
- [func formIntersection(Data.WritingOptions)](./writingoptions/formintersection%28_%29.md)
- [func formSymmetricDifference(Data.WritingOptions)](./writingoptions/formsymmetricdifference%28_%29.md)
- [func formUnion(Data.WritingOptions)](./writingoptions/formunion%28_%29.md)
- [func insert(Data.WritingOptions) -> (inserted: Bool, memberAfterInsert: Data.WritingOptions)](./writingoptions/insert%28_%29.md)
- [func isSubset(of: Data.WritingOptions) -> Bool](./writingoptions/issubset%28of%29.md)
- [func remove(Data.WritingOptions) -> Data.WritingOptions?](./writingoptions/remove%28_%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Writing Data to a File
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(toFile: String, options: NSData.WritingOptions) throws](./write%28tofile,options%29.md)
  Writes the data object’s bytes to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](./write%28to,atomically%29.md)
  Writes the data object’s bytes to the location specified by a given URL.
- [func write(to: URL, options: NSData.WritingOptions) throws](./write%28to,options%29.md)
  Writes the data object’s bytes to the location specified by a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/writingoptions)*
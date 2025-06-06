# FileManager.SearchPathDomainMask

**Framework**: Foundation  
**Kind**: struct

Domain constants specifying base locations to use when you search for significant directories.

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
struct SearchPathDomainMask
```

#### Overview

These constants are used by the [`urls(for:in:)`](filemanager/urls(for:in:).md) and [`url(for:in:appropriateFor:create:)`](filemanager/url(for:in:appropriatefor:create:).md) methods of FileManager.

## Topics

### Creating a Search Path Domain Mask
- [init(rawValue: UInt)](filemanager/searchpathdomainmask/init(rawvalue:).md)
  Creates a search path domain mask.
### Specifying Search Path Domains
- [static var userDomainMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/userdomainmask.md)
  The user’s home directory—the place to install user’s personal items (`~`).
- [static var localDomainMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/localdomainmask.md)
  The place to install items available to everyone on this machine.
- [static var networkDomainMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/networkdomainmask.md)
  The place to install items available on the network (`/Network`).
- [static var systemDomainMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/systemdomainmask.md)
  A directory for system files provided by Apple (`/System`) .
- [static var allDomainsMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/alldomainsmask.md)
  All domains.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md)
  Options for enumerating the contents of directories.
- [FileManager.SearchPathDirectory](filemanager/searchpathdirectory.md)
  The location of significant directories.
- [struct FileAttributeKey](fileattributekey.md)
  Keys in dictionaries used to get and set file attributes.
- [struct FileAttributeType](fileattributetype.md)
  Values representing a file’s type attribute.
- [struct FileProtectionType](fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.
- [struct URLFileProtection](urlfileprotection.md)
  Protection-level values for a URL resource key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask)*
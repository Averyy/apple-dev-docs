# FileManager.SearchPathDomainMask

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSSearchPathDomainMask : NSUInteger;
```

## Overview

These constants are used by the [`urls(for:in:)`](./urls%28for,in%29.md) and [`url(for:in:appropriateFor:create:)`](./url%28for,in,appropriatefor,create%29.md) methods of FileManager.

## Topics

### Creating a Search Path Domain Mask
- [init(rawValue: UInt)](./searchpathdomainmask/init%28rawvalue%29.md)
  Creates a search path domain mask.
### Specifying Search Path Domains
- [static var userDomainMask: FileManager.SearchPathDomainMask](./searchpathdomainmask/userdomainmask.md)
  The user’s home directory—the place to install user’s personal items (`~`).
- [static var localDomainMask: FileManager.SearchPathDomainMask](./searchpathdomainmask/localdomainmask.md)
  The place to install items available to everyone on this machine.
- [static var networkDomainMask: FileManager.SearchPathDomainMask](./searchpathdomainmask/networkdomainmask.md)
  The place to install items available on the network (`/Network`).
- [static var systemDomainMask: FileManager.SearchPathDomainMask](./searchpathdomainmask/systemdomainmask.md)
  A directory for system files provided by Apple (`/System`) .
- [static var allDomainsMask: FileManager.SearchPathDomainMask](./searchpathdomainmask/alldomainsmask.md)
  All domains.

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

### Supporting Types
- [FileManager.DirectoryEnumerationOptions](./directoryenumerationoptions.md)
  Options for enumerating the contents of directories.
- [FileManager.SearchPathDirectory](./searchpathdirectory.md)
  The location of significant directories.
- [struct FileAttributeKey](../fileattributekey.md)
  Keys in dictionaries used to get and set file attributes.
- [struct FileAttributeType](../fileattributetype.md)
  Values representing a file’s type attribute.
- [struct FileProtectionType](../fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.
- [struct URLFileProtection](../urlfileprotection.md)
  Protection-level values for a URL resource key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask)*
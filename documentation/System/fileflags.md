# FileFlags

**Framework**: System  
**Kind**: struct

File-specific flags found in the `st_flags` property of a `stat` struct or used as input to `chflags()`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct FileFlags
```

#### Overview

> **Note**: Only available on Darwin, FreeBSD, and OpenBSD.

## Topics

### Initializers
- [init(rawValue: CInterop.FileFlags)](fileflags/init(rawvalue:).md)
  Creates a strongly-typed `FileFlags` from the raw C value.
### Instance Properties
- [let rawValue: CInterop.FileFlags](fileflags/rawvalue.md)
  The raw C flags.
### Type Properties
- [static var archived: FileFlags](fileflags/archived.md)
  File has been archived.
- [static var compressed: FileFlags](fileflags/compressed.md)
  File is compressed at the file system level.
- [static var dataVault: FileFlags](fileflags/datavault.md)
  File requires an entitlement for reading and writing.
- [static var dataless: FileFlags](fileflags/dataless.md)
  File is a dataless placeholder (content is stored remotely).
- [static var firmlink: FileFlags](fileflags/firmlink.md)
  File is a firmlink.
- [static var hidden: FileFlags](fileflags/hidden.md)
  File should not be displayed in a GUI.
- [static var noDump: FileFlags](fileflags/nodump.md)
  Do not dump the file during backups.
- [static var opaque: FileFlags](fileflags/opaque.md)
  Directory is opaque when viewed through a union mount.
- [static var restricted: FileFlags](fileflags/restricted.md)
  File requires an entitlement for writing.
- [static var systemAppend: FileFlags](fileflags/systemappend.md)
  Writes to the file may only append.
- [static var systemImmutable: FileFlags](fileflags/systemimmutable.md)
  File may not be changed.
- [static var systemNoUnlink: FileFlags](fileflags/systemnounlink.md)
  File may not be removed or renamed.
- [static var tracked: FileFlags](fileflags/tracked.md)
  File is tracked for the purpose of document IDs.
- [static var userAppend: FileFlags](fileflags/userappend.md)
  Writes to the file may only append.
- [static var userImmutable: FileFlags](fileflags/userimmutable.md)
  File may not be changed.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags)*
# allowsEvicting

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

A value indicating that the system can delete the local copy of the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+ - Deprecated in 13.0
- visionOS 1.0+

> **Deprecated**: use NSFileProviderContentPolicy instead

## Declaration

```swift
static var allowsEvicting: NSFileProviderItemCapabilities { get }
```

```c
NSFileProviderItemCapabilitiesAllowsEvicting
```

## See Also

### Constants
- [static var allowsAddingSubItems: NSFileProviderItemCapabilities](./allowsaddingsubitems.md)
  A value indicating that the user can add subitems.
- [static var allowsContentEnumerating: NSFileProviderItemCapabilities](./allowscontentenumerating.md)
  A value indicating that the item’s contents can be enumerated.
- [static var allowsDeleting: NSFileProviderItemCapabilities](./allowsdeleting.md)
  A value indicating that the item can be deleted.
- [static var allowsReading: NSFileProviderItemCapabilities](./allowsreading.md)
  A value indicating that the value can be read from.
- [static var allowsRenaming: NSFileProviderItemCapabilities](./allowsrenaming.md)
  A value indicating that the item can be renamed.
- [static var allowsReparenting: NSFileProviderItemCapabilities](./allowsreparenting.md)
  A value indicating that the item can be moved.
- [static var allowsTrashing: NSFileProviderItemCapabilities](./allowstrashing.md)
  A value indicating that the item can be moved to the trash.
- [static var allowsWriting: NSFileProviderItemCapabilities](./allowswriting.md)
  A value indicating that the item can be written to.
- [static var allowsExcludingFromSync: NSFileProviderItemCapabilities](./allowsexcludingfromsync.md)
  A value indicating that the user can exclude the item from sync operations.
- [static var allowsAll: NSFileProviderItemCapabilities](./allowsall.md)
  A convenience value for enabling all capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemcapabilities/allowsevicting)*
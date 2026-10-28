# allowsExcludingFromSync

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

A value indicating that the user can exclude the item from sync operations.

**Availability**:
- macOS 11.3+

## Declaration

```swift
static var allowsExcludingFromSync: NSFileProviderItemCapabilities { get }
```

```c
NSFileProviderItemCapabilitiesAllowsExcludingFromSync
```

## Discussion

The user can choose to exclude the item from syncs (for example, in Finder’s user interface). If the user excludes an item, the system stops monitoring changes for the item and its children, and removes the item from the file provider.

## See Also

### Constants
- [static var allowsAddingSubItems: NSFileProviderItemCapabilities](./allowsaddingsubitems.md)
  A value indicating that the user can add subitems.
- [static var allowsContentEnumerating: NSFileProviderItemCapabilities](./allowscontentenumerating.md)
  A value indicating that the item’s contents can be enumerated.
- [static var allowsDeleting: NSFileProviderItemCapabilities](./allowsdeleting.md)
  A value indicating that the item can be deleted.
- [static var allowsEvicting: NSFileProviderItemCapabilities](./allowsevicting.md)
  A value indicating that the system can delete the local copy of the item.
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
- [static var allowsAll: NSFileProviderItemCapabilities](./allowsall.md)
  A convenience value for enabling all capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemcapabilities/allowsexcludingfromsync)*
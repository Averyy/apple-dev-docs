# Finder Sync

**Framework**: Finder Sync  
**Kind**: module

Modify the Finder’s user interface to express file synchronization and control.

**Availability**:
- macOS 10.10+

#### Overview

Use Finder Sync to cleanly and safely modify the Finder’s user interface to express file synchronization status and control. Unlike most extension points, Finder Sync doesn’t add features to a host app. Instead, it lets you modify the behavior of the Finder itself.

Use this framework when you need to synchronize the contents of a local folder with a remote data source. Then provide visual feedback to the Finder by extending the [`FIFinderSync`](fifindersync-swift.class.md) class and overriding appearance methods defined within the [`FIFinderSyncProtocol`](fifindersyncprotocol.md) protocol.

To learn more about creating a Finder Sync extension, see [`Finder Sync`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Finder.html#//apple_ref/doc/uid/TP40014214-CH15) in [`App Extension Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Topics

### Classes
- [class FIFinderSync](fifindersync-swift.class.md)
  A type to subclass to add badges, custom shortcut menus, and toolbar buttons to the Finder.
- [class FIFinderSyncController](fifindersynccontroller.md)
  A controller that acts as a bridge between your Finder Sync extension and the Finder itself.
### Protocols
- [protocol FIFinderSyncProtocol](fifindersyncprotocol.md)
  The group of methods to implement for modifying the Finder user interface to express file synchronization status and control.
### Reference
- [FinderSync Enumerations](findersyncenumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/FinderSync)*
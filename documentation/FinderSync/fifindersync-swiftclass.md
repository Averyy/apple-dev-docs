# FIFinderSync

**Framework**: Finder Sync  
**Kind**: class

A type to subclass to add badges, custom shortcut menus, and toolbar buttons to the Finder.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class FIFinderSync
```

#### Overview

Subclass the FIFinderSync class when you want to customize the appearance of the Finder. Although the FIFinderSync class doesn’t provide any developer accessible API, it does adopt the [`FIFinderSyncProtocol`](fifindersyncprotocol.md) protocol. This protocol declares methods you can implement to modify the appearance of the Finder. For more information on these methods, see [`FIFinderSyncProtocol`](fifindersyncprotocol.md). To learn more about creating a Finder Sync extension, see [`Finder Sync`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Finder.html#//apple_ref/doc/uid/TP40014214-CH15) in [`App Extension Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [FIFinderSyncProtocol](fifindersyncprotocol.md)
- [Hashable](../Swift/Hashable.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol FIFinderSyncProtocol](fifindersyncprotocol.md)
  The group of methods to implement for modifying the Finder user interface to express file synchronization status and control.
- [class FIFinderSyncController](fifindersynccontroller.md)
  A controller that acts as a bridge between your Finder Sync extension and the Finder itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersync-swift.class)*
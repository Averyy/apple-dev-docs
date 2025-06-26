# BADownloaderExtensionConfiguration

**Framework**: Background Assets  
**Kind**: protocol

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency protocol BADownloaderExtensionConfiguration : AppExtensionConfiguration
```

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [ManagedDownloaderExtensionConfiguration](manageddownloaderextensionconfiguration.md)

## See Also

- [class BADownloadManager](badownloadmanager.md)
  An object that manages the queue of scheduled asset downloads.
- [protocol BADownloaderExtension](badownloaderextension-qwaw.md)
  An interface for reacting to app life-cycle events and processing concluded asset downloads while your app isn’t running.
- [Downloading essential assets in the background](downloading-essential-assets-in-the-background.md)
  Fetch the assets your app requires before its first launch using an app extension and the Background Assets framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextensionconfiguration)*
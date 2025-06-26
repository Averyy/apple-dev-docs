# ManagedDownloaderExtensionConfiguration

**Framework**: Background Assets  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency protocol ManagedDownloaderExtensionConfiguration : BADownloaderExtensionConfiguration
```

## Topics

### Associated Types
- [associatedtype DownloadManagerDelegateType : BADownloadManagerDelegate, Sendable](manageddownloaderextensionconfiguration/downloadmanagerdelegatetype.md)
### Type Properties
- [static var downloadManagerDelegate: Self.DownloadManagerDelegateType](manageddownloaderextensionconfiguration/downloadmanagerdelegate.md)

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [BADownloaderExtensionConfiguration](badownloaderextensionconfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/manageddownloaderextensionconfiguration)*
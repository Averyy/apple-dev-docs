# CNResourceStatus

**Framework**: Cinematic  
**Kind**: enum

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
enum CNResourceStatus
```

## Topics

### Enumeration Cases
- [CNResourceStatus.needsDownloading](cnresourcestatus/needsdownloading.md)
  Configuration is supported but requires download of resources
- [CNResourceStatus.ready](cnresourcestatus/ready.md)
  Configuration is supported
- [CNResourceStatus.unsupportedAsset](cnresourcestatus/unsupportedasset.md)
  The given asset is unsupported on the current build
- [CNResourceStatus.unsupportedDevice](cnresourcestatus/unsupporteddevice.md)
  The device lacks hardware capabilities for the given configuration
### Initializers
- [init?(rawValue: Int)](cnresourcestatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnresourcestatus)*
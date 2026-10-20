# CNResourceStatus

**Framework**: Cinematic  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CNResourceStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [CNResourceStatus.needsDownloading](./cnresourcestatus/needsdownloading.md)
  Configuration is supported but requires download of resources
- [CNResourceStatus.ready](./cnresourcestatus/ready.md)
  Configuration is supported
- [CNResourceStatus.unsupportedAsset](./cnresourcestatus/unsupportedasset.md)
  The given asset is unsupported on the current build
- [CNResourceStatus.unsupportedDevice](./cnresourcestatus/unsupporteddevice.md)
  The device lacks hardware capabilities for the given configuration
### Initializers
- [init?(rawValue: Int)](./cnresourcestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnresourcestatus)*
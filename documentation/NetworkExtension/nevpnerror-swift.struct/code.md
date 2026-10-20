# NEVPNError.Code

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

Codes that indicate the source of an error.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum NEVPNError : NSInteger;
```

## Topics

### Error codes
- [NEVPNError.Code.configurationDisabled](./code/configurationdisabled.md)
  An error code indicating the VPN configuration associated with the VPN manager isn’t enabled.
- [NEVPNError.Code.configurationInvalid](./code/configurationinvalid.md)
  An error code indicating the VPN configuration associated with the VPN manager object is invalid.
- [NEVPNError.Code.connectionFailed](./code/connectionfailed.md)
  The connection to the VPN server failed.
- [NEVPNError.Code.configurationStale](./code/configurationstale.md)
  An error code that indicates another process modfied the VPN configuration since the last time the app loaded the configuration.
- [NEVPNError.Code.configurationReadWriteFailed](./code/configurationreadwritefailed.md)
  An error code that indicates an error occurred while reading or writing the Network Extension preferences.
- [NEVPNError.Code.configurationUnknown](./code/configurationunknown.md)
  An error code that indicates that unspecified error occurred.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct/code)*
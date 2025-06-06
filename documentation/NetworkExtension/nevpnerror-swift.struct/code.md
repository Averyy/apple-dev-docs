# NEVPNError.Code

**Framework**: Network Extension  
**Kind**: enum

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

## Topics

### Error codes
- [NEVPNError.Code.configurationDisabled](nevpnerror-swift.struct/code/configurationdisabled.md)
  An error code indicating the VPN configuration associated with the VPN manager isn’t enabled.
- [NEVPNError.Code.configurationInvalid](nevpnerror-swift.struct/code/configurationinvalid.md)
  An error code indicating the VPN configuration associated with the VPN manager object is invalid.
- [NEVPNError.Code.connectionFailed](nevpnerror-swift.struct/code/connectionfailed.md)
  The connection to the VPN server failed.
- [NEVPNError.Code.configurationStale](nevpnerror-swift.struct/code/configurationstale.md)
  An error code that indicates another process modfied the VPN configuration since the last time the app loaded the configuration.
- [NEVPNError.Code.configurationReadWriteFailed](nevpnerror-swift.struct/code/configurationreadwritefailed.md)
  An error code that indicates an error occurred while reading or writing the Network Extension preferences.
- [NEVPNError.Code.configurationUnknown](nevpnerror-swift.struct/code/configurationunknown.md)
  An error code that indicates that unspecified error occurred.
### Initializers
- [init?(rawValue: Int)](nevpnerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct/code)*
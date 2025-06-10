# NEVPNError

**Framework**: Network Extension  
**Kind**: struct

Information about an error encountered while configuring or using a VPN.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct NEVPNError
```

## Topics

### Inspecting error properties
- [NEVPNError.Code](nevpnerror-swift.struct/code.md)
  Codes that indicate the source of an error.
### Error codes
- [static var configurationDisabled: NEVPNError.Code](nevpnerror-swift.struct/configurationdisabled.md)
  An error code that indicates the VPN configuration associated with the VPN manager isn’t enabled.
- [static var configurationInvalid: NEVPNError.Code](nevpnerror-swift.struct/configurationinvalid.md)
  An error code that indicates the VPN configuration associated with the VPN manager object is invalid.
- [static var connectionFailed: NEVPNError.Code](nevpnerror-swift.struct/connectionfailed.md)
  An error code that indicates the connection to the VPN server failed.
- [static var configurationStale: NEVPNError.Code](nevpnerror-swift.struct/configurationstale.md)
  An error code that indicates another process modfied the VPN configuration since the last time the app loaded the configuration.
- [static var configurationReadWriteFailed: NEVPNError.Code](nevpnerror-swift.struct/configurationreadwritefailed.md)
  An error code that indicates an error occurred while reading or writing the Network Extension preferences.
- [static var configurationUnknown: NEVPNError.Code](nevpnerror-swift.struct/configurationunknown.md)
  An error code that indicates that unspecified error occurred.
### Type Properties
- [static var errorDomain: String](nevpnerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct)*
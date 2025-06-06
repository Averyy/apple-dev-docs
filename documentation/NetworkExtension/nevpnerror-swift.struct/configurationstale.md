# configurationStale

**Framework**: Network Extension  
**Kind**: property

An error code that indicates another process modfied the VPN configuration since the last time the app loaded the configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static var configurationStale: NEVPNError.Code { get }
```

#### Discussion

This error also occurs if the app tries to save the VPN configuration before loading it from the Network Extension preferences the first time after the app launches.

## See Also

- [static var configurationDisabled: NEVPNError.Code](nevpnerror-swift.struct/configurationdisabled.md)
  An error code that indicates the VPN configuration associated with the VPN manager isn’t enabled.
- [static var configurationInvalid: NEVPNError.Code](nevpnerror-swift.struct/configurationinvalid.md)
  An error code that indicates the VPN configuration associated with the VPN manager object is invalid.
- [static var connectionFailed: NEVPNError.Code](nevpnerror-swift.struct/connectionfailed.md)
  An error code that indicates the connection to the VPN server failed.
- [static var configurationReadWriteFailed: NEVPNError.Code](nevpnerror-swift.struct/configurationreadwritefailed.md)
  An error code that indicates an error occurred while reading or writing the Network Extension preferences.
- [static var configurationUnknown: NEVPNError.Code](nevpnerror-swift.struct/configurationunknown.md)
  An error code that indicates that unspecified error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct/configurationstale)*
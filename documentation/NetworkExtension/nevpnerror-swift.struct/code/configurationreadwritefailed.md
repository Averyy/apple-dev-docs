# NEVPNError.Code.configurationReadWriteFailed

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

An error code that indicates an error occurred while reading or writing the Network Extension preferences.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case configurationReadWriteFailed
```

```c
NEVPNErrorConfigurationReadWriteFailed
```

## See Also

### Error codes
- [NEVPNError.Code.configurationDisabled](./configurationdisabled.md)
  An error code indicating the VPN configuration associated with the VPN manager isn’t enabled.
- [NEVPNError.Code.configurationInvalid](./configurationinvalid.md)
  An error code indicating the VPN configuration associated with the VPN manager object is invalid.
- [NEVPNError.Code.connectionFailed](./connectionfailed.md)
  The connection to the VPN server failed.
- [NEVPNError.Code.configurationStale](./configurationstale.md)
  An error code that indicates another process modfied the VPN configuration since the last time the app loaded the configuration.
- [NEVPNError.Code.configurationUnknown](./configurationunknown.md)
  An error code that indicates that unspecified error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct/code/configurationreadwritefailed)*
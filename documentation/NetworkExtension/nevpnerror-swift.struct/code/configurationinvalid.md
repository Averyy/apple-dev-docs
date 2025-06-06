# NEVPNError.Code.configurationInvalid

**Framework**: Network Extension  
**Kind**: case

An error code indicating the VPN configuration associated with the VPN manager object is invalid.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case configurationInvalid
```

#### Discussion

This error can occur in the following situations:

- The app or extension tried to save the configuration, but the configuration has missing or invalid configuration properties.
- The app or extension tried to use the configuration before being successfully saved to the Network Extension preferences.
- The app or extension tried to use the configuration before being successfully loaded from the Network Extension preferences.

## See Also

- [NEVPNError.Code.configurationDisabled](nevpnerror-swift.struct/code/configurationdisabled.md)
  An error code indicating the VPN configuration associated with the VPN manager isn’t enabled.
- [NEVPNError.Code.connectionFailed](nevpnerror-swift.struct/code/connectionfailed.md)
  The connection to the VPN server failed.
- [NEVPNError.Code.configurationStale](nevpnerror-swift.struct/code/configurationstale.md)
  An error code that indicates another process modfied the VPN configuration since the last time the app loaded the configuration.
- [NEVPNError.Code.configurationReadWriteFailed](nevpnerror-swift.struct/code/configurationreadwritefailed.md)
  An error code that indicates an error occurred while reading or writing the Network Extension preferences.
- [NEVPNError.Code.configurationUnknown](nevpnerror-swift.struct/code/configurationunknown.md)
  An error code that indicates that unspecified error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct/code/configurationinvalid)*
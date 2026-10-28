# configurationInvalid

**Framework**: Network Extension  
**Kind**: property  
**Role**: Type Property

An error code that indicates the VPN configuration associated with the VPN manager object is invalid.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static var configurationInvalid: NEVPNError.Code { get }
```

## Discussion

This error can occur in the following situations:

- The app or extension tried to save the configuration, but the configuration has missing or invalid configuration properties.
- The app or extension tried to use the configuration before being successfully saved to the Network Extension preferences.
- The app or extension tried to use the configuration before being successfully loaded from the Network Extension preferences.

## See Also

### Error codes
- [static var configurationDisabled: NEVPNError.Code](./configurationdisabled.md)
  An error code that indicates the VPN configuration associated with the VPN manager isn’t enabled.
- [static var connectionFailed: NEVPNError.Code](./connectionfailed.md)
  An error code that indicates the connection to the VPN server failed.
- [static var configurationStale: NEVPNError.Code](./configurationstale.md)
  An error code that indicates another process modfied the VPN configuration since the last time the app loaded the configuration.
- [static var configurationReadWriteFailed: NEVPNError.Code](./configurationreadwritefailed.md)
  An error code that indicates an error occurred while reading or writing the Network Extension preferences.
- [static var configurationUnknown: NEVPNError.Code](./configurationunknown.md)
  An error code that indicates that unspecified error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct/configurationinvalid)*
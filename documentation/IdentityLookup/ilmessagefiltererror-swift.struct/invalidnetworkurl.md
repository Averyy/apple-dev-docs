# invalidNetworkURL

**Framework**: SMS and Call Reporting  
**Kind**: property

The network request URL given by the `ILMessageFilterExtensionNetworkURL` key in the app extension’s information property list file is either missing or invalid.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
static var invalidNetworkURL: ILMessageFilterError.Code { get }
```

## See Also

- [static var networkRequestFailed: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/networkrequestfailed.md)
  The network request failed.
- [static var networkURLUnauthorized: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/networkurlunauthorized.md)
  The app extension’s containing app isn’t authorized to allow the app extension to defer network requests to the host specified in its information property list file.
- [static var redundantNetworkDeferral: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/redundantnetworkdeferral.md)
  The app extension tried to defer a request to its network service more than once, which isn’t allowed.
- [static var system: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/system.md)
  An unspecified system error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltererror-swift.struct/invalidnetworkurl)*
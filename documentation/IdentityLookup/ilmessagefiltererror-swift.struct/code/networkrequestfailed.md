# ILMessageFilterError.Code.networkRequestFailed

**Framework**: SMS and Call Reporting  
**Kind**: case

The network request failed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
case networkRequestFailed
```

#### Discussion

The network request failed (the `NSUnderlyingErrorKey` in the [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary of the [`ILMessageFilterError`](ilmessagefiltererror-swift.struct.md) may have additional details).

## See Also

- [ILMessageFilterError.Code.system](ilmessagefiltererror-swift.struct/code/system.md)
  An unspecified system error occurred.
- [ILMessageFilterError.Code.invalidNetworkURL](ilmessagefiltererror-swift.struct/code/invalidnetworkurl.md)
  The network request URL given by the `ILMessageFilterExtensionNetworkURL` key in the app extension’s `Info.plist` file is either missing or invalid.
- [ILMessageFilterError.Code.networkURLUnauthorized](ilmessagefiltererror-swift.struct/code/networkurlunauthorized.md)
  The app extension’s containing app isn’t authorized to allow the app extension to defer network requests to the host specified in its `Info.plist` file.
- [ILMessageFilterError.Code.redundantNetworkDeferral](ilmessagefiltererror-swift.struct/code/redundantnetworkdeferral.md)
  The app extension tried to defer a request to its network service more than once, which isn’t allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltererror-swift.struct/code/networkrequestfailed)*
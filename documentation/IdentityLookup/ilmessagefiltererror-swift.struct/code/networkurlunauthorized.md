# ILMessageFilterError.Code.networkURLUnauthorized

**Framework**: SMS and Call Reporting  
**Kind**: case

The app extension’s containing app isn’t authorized to allow the app extension to defer network requests to the host specified in its `Info.plist` file.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
case networkURLUnauthorized
```

## See Also

- [ILMessageFilterError.Code.system](ilmessagefiltererror-swift.struct/code/system.md)
  An unspecified system error occurred.
- [ILMessageFilterError.Code.invalidNetworkURL](ilmessagefiltererror-swift.struct/code/invalidnetworkurl.md)
  The network request URL given by the `ILMessageFilterExtensionNetworkURL` key in the app extension’s `Info.plist` file is either missing or invalid.
- [ILMessageFilterError.Code.networkRequestFailed](ilmessagefiltererror-swift.struct/code/networkrequestfailed.md)
  The network request failed.
- [ILMessageFilterError.Code.redundantNetworkDeferral](ilmessagefiltererror-swift.struct/code/redundantnetworkdeferral.md)
  The app extension tried to defer a request to its network service more than once, which isn’t allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltererror-swift.struct/code/networkurlunauthorized)*
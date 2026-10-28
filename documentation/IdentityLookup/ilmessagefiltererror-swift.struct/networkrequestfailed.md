# networkRequestFailed

**Framework**: SMS and Call Reporting  
**Kind**: property  
**Role**: Type Property

The network request failed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
static var networkRequestFailed: ILMessageFilterError.Code { get }
```

## Discussion

The network request failed; the `NSUnderlyingErrorKey` in the [`errorUserInfo`](../../Foundation/customnserror/erroruserinfo-1aas5.md) dictionary may have additional details.

## See Also

### Error Codes
- [static var invalidNetworkURL: ILMessageFilterError.Code](./invalidnetworkurl.md)
  The network request URL given by the `ILMessageFilterExtensionNetworkURL` key in the app extension’s information property list file is either missing or invalid.
- [static var networkURLUnauthorized: ILMessageFilterError.Code](./networkurlunauthorized.md)
  The app extension’s containing app isn’t authorized to allow the app extension to defer network requests to the host specified in its information property list file.
- [static var redundantNetworkDeferral: ILMessageFilterError.Code](./redundantnetworkdeferral.md)
  The app extension tried to defer a request to its network service more than once, which isn’t allowed.
- [static var system: ILMessageFilterError.Code](./system.md)
  An unspecified system error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltererror-swift.struct/networkrequestfailed)*
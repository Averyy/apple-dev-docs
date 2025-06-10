# ILMessageFilterError

**Framework**: SMS and Call Reporting  
**Kind**: struct

An error type that indicates problems with network requests and responses related to IdentityLookup APIs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
struct ILMessageFilterError
```

## Topics

### Enumerations
- [ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/code.md)
  IdentityLookup error codes.
### Error Codes
- [static var invalidNetworkURL: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/invalidnetworkurl.md)
  The network request URL given by the `ILMessageFilterExtensionNetworkURL` key in the app extension’s information property list file is either missing or invalid.
- [static var networkRequestFailed: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/networkrequestfailed.md)
  The network request failed.
- [static var networkURLUnauthorized: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/networkurlunauthorized.md)
  The app extension’s containing app isn’t authorized to allow the app extension to defer network requests to the host specified in its information property list file.
- [static var redundantNetworkDeferral: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/redundantnetworkdeferral.md)
  The app extension tried to defer a request to its network service more than once, which isn’t allowed.
- [static var system: ILMessageFilterError.Code](ilmessagefiltererror-swift.struct/system.md)
  An unspecified system error occurred.
### Error Domain
- [let ILMessageFilterErrorDomain: String](ilmessagefiltererrordomain.md)
  The error domain for errors associated with the IdentityLookup APIs.
### Type Properties
- [static var errorDomain: String](ilmessagefiltererror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let ILMessageFilterErrorDomain: String](ilmessagefiltererrordomain.md)
  The error domain for errors associated with the IdentityLookup APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltererror-swift.struct)*
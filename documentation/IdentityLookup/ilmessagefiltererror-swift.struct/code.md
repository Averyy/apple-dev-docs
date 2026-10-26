# ILMessageFilterError.Code

**Framework**: SMS and Call Reporting  
**Kind**: enum  
**Role**: Enumeration

IdentityLookup error codes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum ILMessageFilterError : NSInteger;
```

## Topics

### Error Codes
- [ILMessageFilterError.Code.system](./code/system.md)
  An unspecified system error occurred.
- [ILMessageFilterError.Code.invalidNetworkURL](./code/invalidnetworkurl.md)
  The network request URL given by the `ILMessageFilterExtensionNetworkURL` key in the app extension’s `Info.plist` file is either missing or invalid.
- [ILMessageFilterError.Code.networkURLUnauthorized](./code/networkurlunauthorized.md)
  The app extension’s containing app isn’t authorized to allow the app extension to defer network requests to the host specified in its `Info.plist` file.
- [ILMessageFilterError.Code.networkRequestFailed](./code/networkrequestfailed.md)
  The network request failed.
- [ILMessageFilterError.Code.redundantNetworkDeferral](./code/redundantnetworkdeferral.md)
  The app extension tried to defer a request to its network service more than once, which isn’t allowed.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [ILMessageFilterErrorDomain](../ilmessagefiltererrordomain.md)
  The error domain for errors associated with the IdentityLookup APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltererror-swift.struct/code)*
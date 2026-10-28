# authenticateComponents:withData:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether given authentication data is valid for a given set of components.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (BOOL) authenticateComponents:(NSArray *) components withData:(NSData *) signature;
```

## Return Value

[`true`](../../Swift/true.md) if the `signature` provided is valid for `components`, otherwise [`false`](../../Swift/false.md).

## Discussion

Use this message for validation of incoming messages. An `NSConnection` object raises an `NSFailedAuthenticationException` on receipt of a remote message the delegate doesn’t authenticate.

## Parameters

- `components`: An array that contains `NSData` and `NSPort` objects belonging to an `NSPortMessage` object. See the [`PortMessage`](../portmessage.md) class specification for more information.
- `signature`: Authentication data created by the delegate of the peer `NSConnection` object with [`authenticationDataForComponents:`](./authenticationdataforcomponents_.md).

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Authenticating
- [- authenticationDataForComponents:](./authenticationdataforcomponents_.md)
  Returns an `NSData` object to be used as an authentication stamp for an outgoing message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnectiondelegate/authenticatecomponents:withdata:)*
# NSNetServices Errors

**Framework**: Foundation

If an error occurs, the delegate error-handling methods return a dictionary with the following keys.

## Topics

### Constants
- [class let errorCode: String](netservice/errorcode-swift.type.property.md)
  This key identifies the error that occurred during the most recent operation.
- [class let errorDomain: String](netservice/errordomain.md)
  This key identifies the originator of the error, which is either the `NSNetService` object or the mach network layer. For most errors, you should not need the value provided by this key.

## See Also

- [NetService.ErrorCode](netservice/errorcode-swift.enum.md)
  These constants identify errors that can occur when accessing net services.
- [NetService.Options](netservice/options.md)
  These constants specify options for a network service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnetservices-errors)*
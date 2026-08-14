# ILNetworkResponse

**Framework**: SMS and Call Reporting  
**Kind**: class

A response to an HTTPS network request performed on behalf of a Message Filter app extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILNetworkResponse
```

#### Overview

To preserve user privacy, a Message Filter app extension can’t contact the server itself. Instead, it tells the system to contact the server and pass back the server’s response.

## Topics

### Getting the Response
- [var urlResponse: HTTPURLResponse](ilnetworkresponse/urlresponse.md)
  Encapsulation of an HTTPS URL response.
### Getting Data from the Response
- [var data: Data](ilnetworkresponse/data.md)
  The data returned in the HTTPS response.
### Initializers
- [init?(coder: NSCoder)](ilnetworkresponse/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class ILMessageFilterQueryResponse](ilmessagefilterqueryresponse.md)
  A response to a message filter query request.
- [enum ILMessageFilterAction](ilmessagefilteraction.md)
  Responds to a received message with a filter action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilnetworkresponse)*
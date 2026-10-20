# ILNetworkResponse

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

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

```objc
@interface ILNetworkResponse : NSObject
```

#### Overview

To preserve user privacy, a Message Filter app extension can’t contact the server itself. Instead, it tells the system to contact the server and pass back the server’s response.

## Topics

### Getting the Response
- [var urlResponse: HTTPURLResponse](./ilnetworkresponse/urlresponse.md)
  Encapsulation of an HTTPS URL response.
### Getting Data from the Response
- [var data: Data](./ilnetworkresponse/data.md)
  The data returned in the HTTPS response.
### Initializers
- [init?(coder: NSCoder)](./ilnetworkresponse/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Responses
- [class ILMessageFilterQueryResponse](./ilmessagefilterqueryresponse.md)
  A response to a message filter query request.
- [enum ILMessageFilterAction](./ilmessagefilteraction.md)
  Responds to a received message with a filter action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilnetworkresponse)*
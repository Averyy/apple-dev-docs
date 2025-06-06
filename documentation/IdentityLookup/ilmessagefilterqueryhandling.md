# ILMessageFilterQueryHandling

**Framework**: SMS and Call Reporting  
**Kind**: protocol

A set of methods implemented by a Message Filter app extension to handle query requests.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol ILMessageFilterQueryHandling : NSObjectProtocol
```

## Mentions

- [Creating a Message Filter App Extension](creating-a-message-filter-app-extension.md)

#### Overview

A Message Filter app extension that adopts this protocol forms a response about the message described in the query, based on information that it either stores locally or receives from an associated network service.

When the app extension defers a query request to a server, the system handles all network communication, passing the request to the server and passing the server’s response back to the app extension.

## Topics

### Handling a Query Request
- [func handle(ILMessageFilterQueryRequest, context: ILMessageFilterExtensionContext, completion: (ILMessageFilterQueryResponse) -> Void)](ilmessagefilterqueryhandling/handle(_:context:completion:).md)
  Evaluates a query request and tells the system how to handle the message represented in the request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ILMessageFilterQueryRequest](ilmessagefilterqueryrequest.md)
  A request for a Message Filter app extension to determine the status of a message received from an unknown sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryhandling)*
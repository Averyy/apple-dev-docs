# ILMessageFilterCapabilitiesQueryHandling

**Framework**: SMS and Call Reporting  
**Kind**: protocol  
**Role**: Protocol

A set of methods implemented by a Message Filter app extension to handle capabilities query requests.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol ILMessageFilterCapabilitiesQueryHandling : NSObjectProtocol
```

```objc
@protocol ILMessageFilterCapabilitiesQueryHandling <NSObject>
```

## Topics

### Handling a Capabilities Query Request
- [func handle(ILMessageFilterCapabilitiesQueryRequest, context: ILMessageFilterExtensionContext, completion: (ILMessageFilterCapabilitiesQueryResponse) -> Void)](./ilmessagefiltercapabilitiesqueryhandling/handle%28_,context,completion%29.md)
  Evaluates a query request and provides a response describing how the system should handle the message it represents.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Queries
- [class ILMessageFilterCapabilitiesQueryRequest](./ilmessagefiltercapabilitiesqueryrequest.md)
  A request to query a Message Filter extension about sharing its sub-category capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltercapabilitiesqueryhandling)*
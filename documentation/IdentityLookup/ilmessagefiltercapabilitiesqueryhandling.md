# ILMessageFilterCapabilitiesQueryHandling

**Framework**: SMS and Call Reporting  
**Kind**: protocol

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

## Topics

### Handling a Capabilities Query Request
- [func handle(ILMessageFilterCapabilitiesQueryRequest, context: ILMessageFilterExtensionContext, completion: (ILMessageFilterCapabilitiesQueryResponse) -> Void)](ilmessagefiltercapabilitiesqueryhandling/handle(_:context:completion:).md)
  Evaluates a query request and provides a response describing how the system should handle the message it represents.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ILMessageFilterCapabilitiesQueryRequest](ilmessagefiltercapabilitiesqueryrequest.md)
  A request to query a Message Filter extension about sharing its sub-category capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltercapabilitiesqueryhandling)*
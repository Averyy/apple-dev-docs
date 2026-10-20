# MobileDocumentDisplayRequest.Response.ValidationOutcome

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

A type that represents how the user validates the mobile document response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum ValidationOutcome
```

## Topics

### Enumeration Cases
- [MobileDocumentDisplayRequest.Response.ValidationOutcome.approved](./validationoutcome-swift.enum/approved.md)
  A message that indicates the user approved the document response.
- [MobileDocumentDisplayRequest.Response.ValidationOutcome.dismissed](./validationoutcome-swift.enum/dismissed.md)
  A message that indicates the user didn’t explicitly approve or reject the document response.
- [MobileDocumentDisplayRequest.Response.ValidationOutcome.rejected](./validationoutcome-swift.enum/rejected.md)
  A message that indicates the user rejected the document response.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the response
- [let validationOutcome: MobileDocumentDisplayRequest.Response.ValidationOutcome](./validationoutcome-swift.property.md)
  The value that indicates how the user validated the mobile document response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/response/validationoutcome-swift.enum)*
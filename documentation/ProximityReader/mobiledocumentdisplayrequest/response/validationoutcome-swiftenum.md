# MobileDocumentDisplayRequest.Response.ValidationOutcome

**Framework**: ProximityReader  
**Kind**: enum

A type that represents how the user validates the mobile document response.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum ValidationOutcome
```

## Topics

### Operators
- [static func == (MobileDocumentDisplayRequest.Response.ValidationOutcome, MobileDocumentDisplayRequest.Response.ValidationOutcome) -> Bool](mobiledocumentdisplayrequest/response/validationoutcome-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MobileDocumentDisplayRequest.Response.ValidationOutcome.approved](mobiledocumentdisplayrequest/response/validationoutcome-swift.enum/approved.md)
  A message that indicates the user approved the document response.
- [MobileDocumentDisplayRequest.Response.ValidationOutcome.dismissed](mobiledocumentdisplayrequest/response/validationoutcome-swift.enum/dismissed.md)
  A message that indicates the user didn’t explicitly approve or reject the document response.
- [MobileDocumentDisplayRequest.Response.ValidationOutcome.rejected](mobiledocumentdisplayrequest/response/validationoutcome-swift.enum/rejected.md)
  A message that indicates the user rejected the document response.
### Instance Properties
- [var hashValue: Int](mobiledocumentdisplayrequest/response/validationoutcome-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentdisplayrequest/response/validationoutcome-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledocumentdisplayrequest/response/validationoutcome-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let validationOutcome: MobileDocumentDisplayRequest.Response.ValidationOutcome](mobiledocumentdisplayrequest/response/validationoutcome-swift.property.md)
  The value that indicates how the user validated the mobile document response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/response/validationoutcome-swift.enum)*
# MobileNationalIDCardDisplayRequest.Response.ValidationOutcome

**Framework**: ProximityReader  
**Kind**: enum

A type that represents how the user validates the mobile document response.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
enum ValidationOutcome
```

## Topics

### Operators
- [static func == (MobileNationalIDCardDisplayRequest.Response.ValidationOutcome, MobileNationalIDCardDisplayRequest.Response.ValidationOutcome) -> Bool](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MobileNationalIDCardDisplayRequest.Response.ValidationOutcome.approved](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum/approved.md)
  A message that indicates the user approved the document response.
- [MobileNationalIDCardDisplayRequest.Response.ValidationOutcome.dismissed](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum/dismissed.md)
  A message that indicates the user didn’t explicitly approve or reject the document response.
- [MobileNationalIDCardDisplayRequest.Response.ValidationOutcome.rejected](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum/rejected.md)
  A message that indicates the user rejected the document response.
### Instance Properties
- [var hashValue: Int](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum)*
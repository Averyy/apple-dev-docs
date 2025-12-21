# MobileDocumentDisplayRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type that represents an element you can request from a mobile document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static let age: MobileDocumentDisplayRequest.Element](mobiledocumentdisplayrequest/element/age.md)
  The mobile document holder’s age in years.
- [static let familyName: MobileDocumentDisplayRequest.Element](mobiledocumentdisplayrequest/element/familyname.md)
  The mobile document holder’s family name or last name.
- [static let givenName: MobileDocumentDisplayRequest.Element](mobiledocumentdisplayrequest/element/givenname.md)
  The mobile document holder’s given name or first name.
### Type Methods
- [static func ageAtLeast(Int) -> MobileDocumentDisplayRequest.Element](mobiledocumentdisplayrequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the mobile document holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(elements: [MobileDocumentDisplayRequest.Element], options: MobileDocumentDisplayRequest.Options)](mobiledocumentdisplayrequest/init(elements:options:).md)
  Creates a new mobile document display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/element)*
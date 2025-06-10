# MobileDocumentDisplayRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type that represents an element you can request from a mobile document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Element
```

## Topics

### Operators
- [static func == (MobileDocumentDisplayRequest.Element, MobileDocumentDisplayRequest.Element) -> Bool](mobiledocumentdisplayrequest/element/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledocumentdisplayrequest/element/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentdisplayrequest/element/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
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
### Default Implementations
- [Equatable Implementations](mobiledocumentdisplayrequest/element/equatable-implementations.md)

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
# MobileNationalIDCardDisplayRequest.Element

**Framework**: ProximityReader  
**Kind**: struct

A type that represents an element you can request from a mobile national ID card.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Element
```

## Topics

### Operators
- [static func == (MobileNationalIDCardDisplayRequest.Element, MobileNationalIDCardDisplayRequest.Element) -> Bool](mobilenationalidcarddisplayrequest/element/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobilenationalidcarddisplayrequest/element/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcarddisplayrequest/element/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let age: MobileNationalIDCardDisplayRequest.Element](mobilenationalidcarddisplayrequest/element/age.md)
  The mobile national ID card holder’s age in years.
- [static let familyName: MobileNationalIDCardDisplayRequest.Element](mobilenationalidcarddisplayrequest/element/familyname.md)
  The mobile national ID card holder’s family name or last name.
- [static let givenName: MobileNationalIDCardDisplayRequest.Element](mobilenationalidcarddisplayrequest/element/givenname.md)
  The mobile national ID card holder’s given name or first name.
### Type Methods
- [static func ageAtLeast(Int) -> MobileNationalIDCardDisplayRequest.Element](mobilenationalidcarddisplayrequest/element/ageatleast(_:).md)
  A Boolean value that indicates whether the mobile national ID card holder’s age is at least the given age.
### Default Implementations
- [Equatable Implementations](mobilenationalidcarddisplayrequest/element/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var region: Locale.Region](mobilenationalidcarddisplayrequest/region.md)
  The region of the document you’re requesting.
- [var elements: [MobileNationalIDCardDisplayRequest.Element]](mobilenationalidcarddisplayrequest/elements.md)
  The document elements you’re requesting.
- [var options: MobileNationalIDCardDisplayRequest.Options](mobilenationalidcarddisplayrequest/options-swift.property.md)
  An object that customizes how to perform a display request.
- [MobileNationalIDCardDisplayRequest.Options](mobilenationalidcarddisplayrequest/options-swift.struct.md)
  An object that customizes how to perform a display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest/element)*
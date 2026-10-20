# MobileNationalIDCardDisplayRequest.Element

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that represents an element you can request from a mobile national ID card.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static let age: MobileNationalIDCardDisplayRequest.Element](./element/age.md)
  The mobile national ID card holder’s age in years.
- [static let familyName: MobileNationalIDCardDisplayRequest.Element](./element/familyname.md)
  The mobile national ID card holder’s family name or last name.
- [static let givenName: MobileNationalIDCardDisplayRequest.Element](./element/givenname.md)
  The mobile national ID card holder’s given name or first name.
- [static let name: MobileNationalIDCardDisplayRequest.Element](./element/name.md)
  The mobile national ID card holder’s name.
### Type Methods
- [static func ageAtLeast(Int) -> MobileNationalIDCardDisplayRequest.Element](./element/ageatleast%28_%29.md)
  A Boolean value that indicates whether the mobile national ID card holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the request details
- [var region: Locale.Region](./region.md)
  The region of the document you’re requesting.
- [var elements: [MobileNationalIDCardDisplayRequest.Element]](./elements.md)
  The document elements you’re requesting.
- [var options: MobileNationalIDCardDisplayRequest.Options](./options-swift.property.md)
  An object that customizes how to perform a display request.
- [MobileNationalIDCardDisplayRequest.Options](./options-swift.struct.md)
  An object that customizes how to perform a display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest/element)*
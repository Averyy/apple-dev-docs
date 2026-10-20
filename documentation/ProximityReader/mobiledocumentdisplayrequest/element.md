# MobileDocumentDisplayRequest.Element

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that represents an element you can request from a mobile document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static let age: MobileDocumentDisplayRequest.Element](./element/age.md)
  The mobile document holder’s age in years.
- [static let familyName: MobileDocumentDisplayRequest.Element](./element/familyname.md)
  The mobile document holder’s family name or last name.
- [static let givenName: MobileDocumentDisplayRequest.Element](./element/givenname.md)
  The mobile document holder’s given name or first name.
- [static let name: MobileDocumentDisplayRequest.Element](./element/name.md)
  The mobile document holder’s name.
### Type Methods
- [static func ageAtLeast(Int) -> MobileDocumentDisplayRequest.Element](./element/ageatleast%28_%29.md)
  A Boolean value that indicates whether the mobile document holder’s age is at least the given age.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a display request
- [init(elements: [MobileDocumentDisplayRequest.Element], options: MobileDocumentDisplayRequest.Options)](./init%28elements,options%29.md)
  Creates a new mobile document display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/element)*
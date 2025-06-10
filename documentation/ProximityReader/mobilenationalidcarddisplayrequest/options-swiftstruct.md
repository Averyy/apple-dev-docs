# MobileNationalIDCardDisplayRequest.Options

**Framework**: ProximityReader  
**Kind**: struct

An object that customizes how to perform a display request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Options
```

#### Overview

Use this object to configure the validation mode of the request.

## Topics

### Structures
- [MobileNationalIDCardDisplayRequest.Options.ValidationMode](mobilenationalidcarddisplayrequest/options-swift.struct/validationmode-swift.struct.md)
  A type that represents the validation mode of the mobile document request.
### Operators
- [static func == (MobileNationalIDCardDisplayRequest.Options, MobileNationalIDCardDisplayRequest.Options) -> Bool](mobilenationalidcarddisplayrequest/options-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(validationMode: MobileNationalIDCardDisplayRequest.Options.ValidationMode)](mobilenationalidcarddisplayrequest/options-swift.struct/init(validationmode:).md)
  Creates a mobile document reader display request options type.
### Instance Properties
- [var hashValue: Int](mobilenationalidcarddisplayrequest/options-swift.struct/hashvalue.md)
  The hash value.
- [var validationMode: MobileNationalIDCardDisplayRequest.Options.ValidationMode](mobilenationalidcarddisplayrequest/options-swift.struct/validationmode-swift.property.md)
  The validation mode of the mobile document request.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcarddisplayrequest/options-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobilenationalidcarddisplayrequest/options-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var region: Locale.Region](mobilenationalidcarddisplayrequest/region.md)
  The region of the document you’re requesting.
- [var elements: [MobileNationalIDCardDisplayRequest.Element]](mobilenationalidcarddisplayrequest/elements.md)
  The document elements you’re requesting.
- [MobileNationalIDCardDisplayRequest.Element](mobilenationalidcarddisplayrequest/element.md)
  A type that represents an element you can request from a mobile national ID card.
- [var options: MobileNationalIDCardDisplayRequest.Options](mobilenationalidcarddisplayrequest/options-swift.property.md)
  An object that customizes how to perform a display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest/options-swift.struct)*
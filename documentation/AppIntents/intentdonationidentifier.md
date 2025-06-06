# IntentDonationIdentifier

**Framework**: App Intents  
**Kind**: struct

An opaque type that identifies a specific donation to the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct IntentDonationIdentifier
```

## Topics

### Creating an identifier
- [init(from: any Decoder) throws](intentdonationidentifier/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Encoding the type
- [func encode(to: any Encoder) throws](intentdonationidentifier/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing identifiers
- [static func == (IntentDonationIdentifier, IntentDonationIdentifier) -> Bool](intentdonationidentifier/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intentdonationidentifier/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentdonationidentifier/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](intentdonationidentifier/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct IntentDonationManager](intentdonationmanager.md)
  A type you use to donate intents to the system, or delete intents when they become irrelevant.
- [struct IntentDonationMatchingPredicate](intentdonationmatchingpredicate.md)
  The match conditions that identify a set of previously donated app intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationidentifier)*
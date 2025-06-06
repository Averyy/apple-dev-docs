# MobileDocumentReader.Configuration

**Framework**: ProximityReader  
**Kind**: struct

A type that represents the configuration of the mobile document reader.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Configuration
```

#### Overview

Use the reader’s configuration to generate a reader token on your server.

## Topics

### Operators
- [static func == (MobileDocumentReader.Configuration, MobileDocumentReader.Configuration) -> Bool](mobiledocumentreader/configuration-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledocumentreader/configuration-swift.struct/hashvalue.md)
  The hash value.
- [let readerInstanceIdentifier: String](mobiledocumentreader/configuration-swift.struct/readerinstanceidentifier.md)
  The unique identifier for the mobile document reader instance.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentreader/configuration-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledocumentreader/configuration-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var configuration: MobileDocumentReader.Configuration](mobiledocumentreader/configuration-swift.property.md)
  The configuration of the mobile document reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentreader/configuration-swift.struct)*
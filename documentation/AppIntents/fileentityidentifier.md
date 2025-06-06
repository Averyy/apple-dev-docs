# FileEntityIdentifier

**Framework**: App Intents  
**Kind**: struct

An identifier for an app entity that refers to a document or other file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct FileEntityIdentifier
```

## Topics

### Operators
- [static func == (FileEntityIdentifier, FileEntityIdentifier) -> Bool](fileentityidentifier/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](fileentityidentifier/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var draftIdentifier: String?](fileentityidentifier/draftidentifier.md)
  The document draft identifier, if the document hasn’t been materialized on disk yet.
- [var fileURL: URL?](fileentityidentifier/fileurl.md)
  A URL that locates a file saved to disk.
- [var hashValue: Int](fileentityidentifier/hashvalue.md)
  The hash value.
- [var isDraft: Bool](fileentityidentifier/isdraft.md)
  Indicates whether this identifier represents a document draft.
### Instance Methods
- [func encode(to: any Encoder) throws](fileentityidentifier/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](fileentityidentifier/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Methods
- [static func draft(identifier: String) -> FileEntityIdentifier](fileentityidentifier/draft(identifier:).md)
  Creates and returns an identifier for a draft document.
- [static func file(url: URL) throws -> FileEntityIdentifier](fileentityidentifier/file(url:).md)
  Creates and returns an identifier with the provided URL to the file on disk.
### Default Implementations
- [EntityIdentifierConvertible Implementations](fileentityidentifier/entityidentifierconvertible-implementations.md)
- [Equatable Implementations](fileentityidentifier/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [EntityIdentifierConvertible](entityidentifierconvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/fileentityidentifier)*
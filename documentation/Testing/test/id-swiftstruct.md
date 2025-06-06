# Test.ID

**Framework**: Swift Testing  
**Kind**: struct

A type representing the stable identity of the entity associated with an instance.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
struct ID
```

## Topics

### Operators
- [static func == (Test.ID, Test.ID) -> Bool](test/id-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](test/id-swift.struct/hashvalue.md)
  The hash value.
- [var moduleName: String](test/id-swift.struct/modulename.md)
  The name of the module containing the corresponding test.
- [var nameComponents: [String]](test/id-swift.struct/namecomponents.md)
  The fully qualified name components (other than the module name) used to identify the corresponding test.
- [var parent: Test.ID?](test/id-swift.struct/parent.md)
  The ID of the parent test.
- [var sourceLocation: SourceLocation?](test/id-swift.struct/sourcelocation.md)
  The source location of the corresponding test.
### Instance Methods
- [func hash(into: inout Hasher)](test/id-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomStringConvertible Implementations](test/id-swift.struct/customstringconvertible-implementations.md)
- [Decodable Implementations](test/id-swift.struct/decodable-implementations.md)
- [Encodable Implementations](test/id-swift.struct/encodable-implementations.md)
- [Equatable Implementations](test/id-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test/id-swift.struct)*
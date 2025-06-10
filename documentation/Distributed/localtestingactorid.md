# LocalTestingActorID

**Framework**: Distributed  
**Kind**: struct

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct LocalTestingActorID
```

## Topics

### Operators
- [static func == (LocalTestingActorID, LocalTestingActorID) -> Bool](localtestingactorid/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](localtestingactorid/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(id: String)](localtestingactorid/init(id:).md)
- [init(parse: String)](localtestingactorid/init(parse:).md)
### Instance Properties
- [var address: String](localtestingactorid/address.md)
- [var hashValue: Int](localtestingactorid/hashvalue.md)
  The hash value.
- [let id: String](localtestingactorid/id.md)
### Instance Methods
- [func encode(to: any Encoder) throws](localtestingactorid/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](localtestingactorid/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](localtestingactorid/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class LocalTestingDistributedActorSystem](localtestingdistributedactorsystem.md)
  A `DistributedActorSystem` designed for local only testing.
- [typealias LocalTestingActorAddress](localtestingactoraddress.md)
- [struct LocalTestingInvocationEncoder](localtestinginvocationencoder.md)
- [class LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)
- [struct LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingactorid)*
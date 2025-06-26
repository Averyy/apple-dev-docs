# DefaultSnapshot

**Framework**: SwiftData  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
struct DefaultSnapshot
```

## Topics

### Initializers
- [init(from: any Decoder) throws](defaultsnapshot/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(from: any BackingData, relatedBackingDatas: inout [PersistentIdentifier : any BackingData])](defaultsnapshot/init(from:relatedbackingdatas:).md)
### Instance Properties
- [let persistentIdentifier: PersistentIdentifier](defaultsnapshot/persistentidentifier.md)
### Instance Methods
- [func copy(persistentIdentifier: PersistentIdentifier, remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier]?) -> DefaultSnapshot](defaultsnapshot/copy(persistentidentifier:remappedidentifiers:).md)
- [func encode(to: any Encoder) throws](defaultsnapshot/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [DataStoreSnapshot](datastoresnapshot.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, DefaultStore.Snapshot>](defaultstore/fetch(_:).md)
- [DefaultStore.Snapshot](defaultstore/snapshot.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](defaultstore/fetchcount(_:).md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](defaultstore/fetchidentifiers(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultsnapshot)*
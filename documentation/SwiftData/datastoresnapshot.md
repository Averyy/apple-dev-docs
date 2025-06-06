# DataStoreSnapshot

**Framework**: SwiftData  
**Kind**: protocol

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
protocol DataStoreSnapshot : Decodable, Encodable, Sendable
```

## Topics

### Initializers
- [init(from: any BackingData, relatedBackingDatas: inout [PersistentIdentifier : any BackingData])](datastoresnapshot/init(from:relatedbackingdatas:).md)
### Instance Properties
- [var persistentIdentifier: PersistentIdentifier](datastoresnapshot/persistentidentifier.md)
### Instance Methods
- [func copy(persistentIdentifier: PersistentIdentifier, remappedIdentifiers: [PersistentIdentifier : PersistentIdentifier]?) -> Self](datastoresnapshot/copy(persistentidentifier:remappedidentifiers:).md)

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DefaultSnapshot](defaultsnapshot.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastoresnapshot)*
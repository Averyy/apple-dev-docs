# DataStoreConfiguration

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
protocol DataStoreConfiguration : Hashable
```

## Topics

### Associated Types
- [associatedtype Store : DataStore](datastoreconfiguration/store.md)
### Instance Properties
- [var name: String](datastoreconfiguration/name.md)
- [var schema: Schema?](datastoreconfiguration/schema.md)
### Instance Methods
- [func validate() throws](datastoreconfiguration/validate.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
### Conforming Types
- [ModelConfiguration](modelconfiguration.md)

## See Also

- [var configuration: Self.Configuration](datastore/configuration-swift.property.md)
- [associatedtype Configuration : DataStoreConfiguration](datastore/configuration-swift.associatedtype.md)
- [var identifier: String](datastore/identifier.md)
- [var schema: Schema](datastore/schema.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastoreconfiguration)*
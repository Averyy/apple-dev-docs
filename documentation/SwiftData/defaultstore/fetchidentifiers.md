# fetchIdentifiers(_:)

**Framework**: SwiftData  
**Kind**: method

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
final func fetchIdentifiers<T>(_ request: DataStoreFetchRequest<T>) throws -> [PersistentIdentifier] where T : PersistentModel
```

## See Also

- [func fetch<T>(DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, DefaultStore.Snapshot>](defaultstore/fetch(_:).md)
- [DefaultStore.Snapshot](defaultstore/snapshot.md)
- [struct DefaultSnapshot](defaultsnapshot.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](defaultstore/fetchcount(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultstore/fetchidentifiers(_:))*
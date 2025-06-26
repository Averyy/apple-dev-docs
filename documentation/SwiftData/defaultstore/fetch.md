# fetch(_:)

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
final func fetch<T>(_ request: DataStoreFetchRequest<T>) throws -> DataStoreFetchResult<T, DefaultStore.Snapshot> where T : PersistentModel
```

## See Also

- [DefaultStore.Snapshot](defaultstore/snapshot.md)
- [struct DefaultSnapshot](defaultsnapshot.md)
- [func fetchCount<T>(DataStoreFetchRequest<T>) throws -> Int](defaultstore/fetchcount(_:).md)
- [func fetchIdentifiers<T>(DataStoreFetchRequest<T>) throws -> [PersistentIdentifier]](defaultstore/fetchidentifiers(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultstore/fetch(_:))*
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultstore/fetch(_:))*
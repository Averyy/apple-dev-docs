# cachedSnapshots(for:editingState:)

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
final func cachedSnapshots(for persistentIdentifiers: [PersistentIdentifier], editingState: EditingState) throws -> [PersistentIdentifier : DefaultStore.Snapshot]
```

## See Also

- [func initializeState(for: EditingState)](defaultstore/initializestate(for:).md)
- [func invalidateState(for: EditingState)](defaultstore/invalidatestate(for:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultstore/cachedsnapshots(for:editingstate:))*
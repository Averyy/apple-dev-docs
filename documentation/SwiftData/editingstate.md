# EditingState

**Framework**: SwiftData  
**Kind**: struct  
**Role**: Structure

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
struct EditingState
```

## Topics

### Instance Properties
- [var author: String?](./editingstate/author.md)

## Relationships

### Conforms To
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sharing cached data between model contexts
- [func initializeState(for: EditingState)](./datastore/initializestate%28for%29.md)
- [func cachedSnapshots(for: [PersistentIdentifier], editingState: EditingState) throws -> [PersistentIdentifier : Self.Snapshot]](./datastore/cachedsnapshots%28for,editingstate%29.md)
- [func invalidateState(for: EditingState)](./datastore/invalidatestate%28for%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/editingstate)*
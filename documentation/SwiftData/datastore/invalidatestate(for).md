# invalidateState(for:)

**Framework**: SwiftData  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

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
func invalidateState(for editingState: EditingState)
```

## Default Implementations

### DataStore Implementations
- [func invalidateState(for: EditingState)](./invalidatestate%28for%29-8z39v.md)

## See Also

### Sharing cached data between model contexts
- [func initializeState(for: EditingState)](./initializestate%28for%29.md)
- [struct EditingState](../editingstate.md)
- [func cachedSnapshots(for: [PersistentIdentifier], editingState: EditingState) throws -> [PersistentIdentifier : Self.Snapshot]](./cachedsnapshots%28for,editingstate%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastore/invalidatestate(for:))*
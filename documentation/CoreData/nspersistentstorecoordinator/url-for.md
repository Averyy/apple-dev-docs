# url(for:)

**Framework**: Core Data  
**Kind**: method

Returns the location of the provided persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func url(for store: NSPersistentStore) -> URL
```

#### Return Value

The URL for `store`.

## Parameters

- `store`: A persistent store.

## See Also

- [var persistentStores: [NSPersistentStore]](nspersistentstorecoordinator/persistentstores.md)
  The coordinator’s persistent stores.
- [func setURL(URL, for: NSPersistentStore) -> Bool](nspersistentstorecoordinator/seturl(_:for:).md)
  Changes the location of the specified persistent store.
- [func persistentStore(for: URL) -> NSPersistentStore?](nspersistentstorecoordinator/persistentstore(for:).md)
  Returns the persistent store for the specified file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/url(for:))*
# url(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the location of the provided persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func url(for store: NSPersistentStore) -> URL
```

```objc
- (NSURL *) URLForPersistentStore:(NSPersistentStore *) store;
```

#### Return Value

The URL for `store`.

## Parameters

- `store`: A persistent store.

## See Also

### Related Documentation
- [var persistentStores: [NSPersistentStore]](./persistentstores.md)
  The coordinator’s persistent stores.
### Managing a store’s location
- [func setURL(URL, for: NSPersistentStore) -> Bool](./seturl%28_,for%29.md)
  Changes the location of the specified persistent store.
- [func persistentStore(for: URL) -> NSPersistentStore?](./persistentstore%28for%29.md)
  Returns the persistent store for the specified file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/url(for:))*
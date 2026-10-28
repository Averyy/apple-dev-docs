# persistentStore(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the persistent store for the specified file URL.

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
func persistentStore(for URL: URL) -> NSPersistentStore?
```

```objc
- (NSPersistentStore *) persistentStoreForURL:(NSURL *) URL;
```

## Return Value

The persistent store at the location specified by `URL`.

## Parameters

- `URL`: An URL object that specifies the location of a persistent store.

## See Also

### Managing a store’s location
- [func setURL(URL, for: NSPersistentStore) -> Bool](./seturl%28_,for%29.md)
  Changes the location of the specified persistent store.
- [func url(for: NSPersistentStore) -> URL](./url%28for%29.md)
  Returns the location of the provided persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/persistentstore(for:))*
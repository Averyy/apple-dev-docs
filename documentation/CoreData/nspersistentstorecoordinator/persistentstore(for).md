# persistentStore(for:)

**Framework**: Core Data  
**Kind**: method

Returns the persistent store for the specified file URL.

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
func persistentStore(for URL: URL) -> NSPersistentStore?
```

#### Return Value

The persistent store at the location specified by `URL`.

## Parameters

- `URL`: An URL object that specifies the location of a persistent store.

## See Also

- [func setURL(URL, for: NSPersistentStore) -> Bool](nspersistentstorecoordinator/seturl(_:for:).md)
  Changes the location of the specified persistent store.
- [func url(for: NSPersistentStore) -> URL](nspersistentstorecoordinator/url(for:).md)
  Returns the location of the provided persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/persistentstore(for:))*
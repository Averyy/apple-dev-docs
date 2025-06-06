# setURL(_:for:)

**Framework**: Core Data  
**Kind**: method

Changes the location of the specified persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setURL(_ url: URL, for store: NSPersistentStore) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the store was relocated, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

For atomic stores, this method alters the location to which the next save operation will write the file; for non-atomic stores, invoking this method will relinquish the existing connection and create a new one at the specified URL. (For non-atomic stores, a store must already exist at the destination URL; a new store will not be created.)

## Parameters

- `url`: The new location for  .
- `store`: A persistent store associated with the receiver.

## See Also

- [func persistentStore(for: URL) -> NSPersistentStore?](nspersistentstorecoordinator/persistentstore(for:).md)
  Returns the persistent store for the specified file URL.
- [func url(for: NSPersistentStore) -> URL](nspersistentstorecoordinator/url(for:).md)
  Returns the location of the provided persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/seturl(_:for:))*
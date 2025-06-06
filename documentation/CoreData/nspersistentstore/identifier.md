# identifier

**Framework**: Core Data  
**Kind**: property

The unique identifier for the persistent store.

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
var identifier: String! { get set }
```

#### Discussion

The identifier is used as part of the managed object IDs for each object in the store.

##### Special Considerations

`NSPersistentStore` provides a default implementation to provide a globally unique identifier for the store instance.

## See Also

- [var metadata: [String : Any]!](nspersistentstore/metadata.md)
  The metadata for the persistent store.
- [var isReadOnly: Bool](nspersistentstore/isreadonly.md)
  A Boolean value that indicates whether the persistent store is read-only.
- [var url: URL?](nspersistentstore/url.md)
  The URL for the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/identifier)*
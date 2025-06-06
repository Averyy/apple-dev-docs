# url

**Framework**: Core Data  
**Kind**: property

The URL for the persistent store.

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
var url: URL? { get set }
```

#### Discussion

To alter the location of a store, send the persistent store coordinator a [`setURL(_:for:)`](nspersistentstorecoordinator/seturl(_:for:).md) message.

## See Also

- [var identifier: String!](nspersistentstore/identifier.md)
  The unique identifier for the persistent store.
- [var isReadOnly: Bool](nspersistentstore/isreadonly.md)
  A Boolean value that indicates whether the persistent store is read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/url)*
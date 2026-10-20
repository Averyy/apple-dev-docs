# identifier

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var identifier: String! { get set }
```

```objc
@property (copy, null_resettable) NSString * identifier;
```

#### Discussion

The identifier is used as part of the managed object IDs for each object in the store.

##### Special Considerations

`NSPersistentStore` provides a default implementation to provide a globally unique identifier for the store instance.

## See Also

### Related Documentation
- [var metadata: [String : Any]!](./metadata.md)
  The metadata for the persistent store.
### Managing Store Attributes
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that indicates whether the persistent store is read-only.
- [var url: URL?](./url.md)
  The URL for the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/identifier)*
# persistentStoreDescriptionWithURL:

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Initializes and returns a persistent store description with the given URL.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
+ (instancetype) persistentStoreDescriptionWithURL:(NSURL *) URL;
```

#### Return Value

Initialized [`NSPersistentStoreDescription`](../nspersistentstoredescription.md) configured with the given URL.

#### Discussion

This method is a convenience for creating a new [`NSPersistentStoreDescription`](../nspersistentstoredescription.md) configured with a given URL.

## Parameters

- `URL`: Location for the store.

## See Also

### Creating a Persistent Store Description
- [init(url: URL)](./init%28url%29-ko0l.md)
  Initializes the receiver with a URL for the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/persistentstoredescriptionwithurl:)*
# init(url:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Initializes the receiver with a URL for the store.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(url: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) url;
```

## Return Value

Initialized [`NSPersistentStoreDescription`](../nspersistentstoredescription.md) configured with the given URL.

## Parameters

- `url`: Location for the store.

## See Also

### Creating a Persistent Store Description
- [+ persistentStoreDescriptionWithURL:](./persistentstoredescriptionwithurl_.md)
  Initializes and returns a persistent store description with the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/init(url:)-ko0l)*
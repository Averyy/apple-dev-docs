# add(from:)

**Framework**: ShazamKit  
**Kind**: method  
**Role**: Instance Method

Loads a saved custom catalog from a file.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func add(from customCatalogURL: URL) throws
```

```objc
- (BOOL) addCustomCatalogFromURL:(NSURL *) customCatalogURL error:(NSError **) error;
```

## Parameters

- `customCatalogURL`: The file URL for a custom catalog.

## See Also

### Loading and saving a custom catalog
- [func write(to: URL) throws](./write%28to%29.md)
  Saves the custom catalog to a local file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shcustomcatalog/add(from:))*
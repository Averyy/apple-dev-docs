# write(to:)

**Framework**: ShazamKit  
**Kind**: method  
**Role**: Instance Method

Saves the custom catalog to a local file.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use dataRepresentation

## Declaration

```swift
func write(to destinationURL: URL) throws
```

```objc
- (BOOL) writeToURL:(NSURL *) destinationURL error:(NSError **) error;
```

## Discussion

If `destinationURL` is a directory, the system creates a `Signatures.shazamcatalog` file.

## Parameters

- `destinationURL`: A URL for the saved custom catalog file.

## See Also

### Loading and saving a custom catalog
- [func add(from: URL) throws](./add%28from%29.md)
  Loads a saved custom catalog from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shcustomcatalog/write(to:))*
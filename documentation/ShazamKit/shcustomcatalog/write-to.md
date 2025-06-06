# write(to:)

**Framework**: ShazamKit  
**Kind**: method

Saves the custom catalog to a local file.

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
func write(to destinationURL: URL) throws
```

#### Discussion

If `destinationURL` is a directory, the system creates a `Signatures.shazamcatalog` file.

## Parameters

- `destinationURL`: A URL for the saved custom catalog file.

## See Also

- [func add(from: URL) throws](shcustomcatalog/add(from:).md)
  Loads a saved custom catalog from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shcustomcatalog/write(to:))*
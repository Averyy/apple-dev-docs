# detectedValues(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func detectedValues(for keyPaths: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> NSPasteboard.DetectedValues
```

#### Return Value

An [`NSPasteboard.DetectedValues`](./detectedvalues.md) instance containing the values for the patterns found on the pasteboard.

#### Discussion

For details about the types returned for each pattern, see [`NSPasteboard.DetectedValues`](./detectedvalues.md).

The following example shows how to use this method to find links in the first pasteboard item:

```swift
do {
    let valueResults = try await NSPasteboard.general.detectedValues(for: [\.links])
    let links = valueResults.links
    guard !links.isEmpty else {
        print ("No links found in item.")
        return
    }
    for link in links {
        print("Link retrieved: \(link.url).")
    }
} catch {
    print("Error: \(error).")
}
```

> ❗ **Important**: When calling this method, if a match is found, the system informs the person using the app that the app is trying to read the contents of the pasteboard. If the person denies access to the pasteboard, the method throws an error.

## Parameters

- `keyPaths`: The patterns to detect on the pasteboard.

## See Also

### Detecting patterns and metadata in pasteboard items
- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboard.DetectedValues>>](./detectedpatterns%28for%29.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the person using the app.
- [NSPasteboard.DetectedValues](./detectedvalues.md)
  A type that contains common types of data that the data detection system matches for a pasteboard.
- [Pasteboard detection patterns](../nspasteboard-detection-patterns.md)
  Common types of data that the data detection system matches for a pasteboard.
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboard.DetectedMetadata>>) async throws -> NSPasteboard.DetectedMetadata](./detectedmetadata%28for%29.md)
  Determines available metadata from the specified metadata types for the first pasteboard item, without notifying the person using the app.
- [NSPasteboard.DetectedMetadata](./detectedmetadata.md)
  An object that contains common types of metadata that the data detection system matches for a pasteboard.
- [Pasteboard detection metadata types](../nspasteboard-detection-metadata-types.md)
  Common types of metadata that the data detection system matches for a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/detectedvalues(for:))*
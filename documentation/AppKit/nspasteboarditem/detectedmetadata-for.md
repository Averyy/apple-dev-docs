# detectedMetadata(for:)

**Framework**: AppKit  
**Kind**: method

Determines available metadata from the specified metadata types for this pasteboard item, without notifying the person using the app.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func detectedMetadata(for keyPaths: Set<PartialKeyPath<NSPasteboardItem.DetectedMetadata>>) async throws -> NSPasteboardItem.DetectedMetadata
```

#### Return Value

An [`NSPasteboard.DetectedMetadata`](nspasteboard/detectedmetadata.md) instance containing the metadata for the metadata types detected on the pasteboard item.

#### Discussion

This method only gives access to limited types of metadata and doesn’t allow the app to access the item’s contents. As a result, the system doesn’t notify the person using the app about reading the contents of the pasteboard.

For details about the metadata returned for each type, see [`NSPasteboard.DetectedMetadata`](nspasteboard/detectedmetadata.md).

The following example shows how to iterate over each pasteboard item and, if the item is a URL that points to a file, get its content type with this method.

```swift
guard let pasteboardItems = NSPasteboard.general.pasteboardItems else { return }
for (index, item) in pasteboardItems.enumerated() {
    do {
        let metadataResults = try await item.detectedMetadata(for: [\.contentType])
        if let contentType = metadataResults.contentType {
            print("Item \(index) - Content type is: \(contentType.identifier).")
        } else {
            print("Item \(index) - Couldn't get content type.")
        }
    } catch {
        print("Item \(index) - Error: \(error).")
    }
}
```

## Parameters

- `keyPaths`: The metadata types to detect on the pasteboard item.

## See Also

- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>](nspasteboarditem/detectedpatterns(for:).md)
  Determines whether the pasteboard item matches the specified patterns, without notifying the person using the app.
- [func detectedValues(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> NSPasteboardItem.DetectedValues](nspasteboarditem/detectedvalues(for:).md)
  Determines whether this pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [NSPasteboardItem.DetectedValues](nspasteboarditem/detectedvalues.md)
- [NSPasteboardItem.DetectedMetadata](nspasteboarditem/detectedmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/detectedmetadata(for:))*
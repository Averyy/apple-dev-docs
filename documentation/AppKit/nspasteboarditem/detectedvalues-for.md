# detectedValues(for:)

**Framework**: AppKit  
**Kind**: method

Determines whether this pasteboard item matches the specified patterns, reading the contents if it finds a match.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func detectedValues(for keyPaths: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> NSPasteboardItem.DetectedValues
```

#### Return Value

An [`NSPasteboard.DetectedValues`](nspasteboard/detectedvalues.md) instance containing the values for the patterns detected on the pasteboard item.

#### Discussion

For details about the types returned for each pattern, see [`NSPasteboard.DetectedValues`](nspasteboard/detectedvalues.md).

The following example shows how to use this method to find links in each item on the pasteboard:

```swift
guard let pasteboardItems = NSPasteboard.general.pasteboardItems else { return }
for (index, item) in pasteboardItems.enumerated() {
    do {
        let valueResults = try await item.detectedValues(for: [\.links])
        let links = valueResults.links
        guard !links.isEmpty else {
            print ("Item \(index) - No links found in item.")
            continue
        }
        for link in links {
            print("Item \(index) - Link retrieved: \(link.url).")
        }
    } catch {
        print("Item \(index) - Error: \(error).")
    }
}
```

> ❗ **Important**: If the system finds a match when calling this method, the system informs the person using the app that the app is trying to read the contents of the pasteboard. If the person denies access to the pasteboard, the method throws an error.

## Parameters

- `keyPaths`: The patterns to detect on the pasteboard.

## See Also

- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>](nspasteboarditem/detectedpatterns(for:).md)
  Determines whether the pasteboard item matches the specified patterns, without notifying the person using the app.
- [NSPasteboardItem.DetectedValues](nspasteboarditem/detectedvalues.md)
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboardItem.DetectedMetadata>>) async throws -> NSPasteboardItem.DetectedMetadata](nspasteboarditem/detectedmetadata(for:).md)
  Determines available metadata from the specified metadata types for this pasteboard item, without notifying the person using the app.
- [NSPasteboardItem.DetectedMetadata](nspasteboarditem/detectedmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/detectedvalues(for:))*
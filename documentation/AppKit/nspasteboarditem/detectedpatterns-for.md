# detectedPatterns(for:)

**Framework**: AppKit  
**Kind**: method

Determines whether the pasteboard item matches the specified patterns, without notifying the person using the app.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func detectedPatterns(for keyPaths: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>
```

#### Return Value

A set with the patterns found on the pasteboard item.

#### Discussion

This method only gives an indication of whether a pasteboard item matches a particular pattern and doesn’t allow the app to access the contents. As a result, the system doesn’t notify the person using the app about reading the contents of the pasteboard.

The following example shows how to use this method to find calendar events in each item on the pasteboard:

```swift
guard let pasteboardItems = NSPasteboard.general.pasteboardItems else { return }
for (index, item) in pasteboardItems.enumerated() {
    do {
        let patternResults = try await item.detectedPatterns(for: [\.calendarEvents])
        if patternResults.contains(\.calendarEvents) {
            print("Item \(index) - Calendar event(s) detected.")
        } else {
            print("Item \(index) - Didn't detect any calendar events.")
        }
    } catch {
        print("Item \(index) - Error: \(error).")
    }
}
```

## Parameters

- `keyPaths`: The patterns to detect on the pasteboard item.

## See Also

- [func detectedValues(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> NSPasteboardItem.DetectedValues](nspasteboarditem/detectedvalues(for:).md)
  Determines whether this pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [NSPasteboardItem.DetectedValues](nspasteboarditem/detectedvalues.md)
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboardItem.DetectedMetadata>>) async throws -> NSPasteboardItem.DetectedMetadata](nspasteboarditem/detectedmetadata(for:).md)
  Determines available metadata from the specified metadata types for this pasteboard item, without notifying the person using the app.
- [NSPasteboardItem.DetectedMetadata](nspasteboarditem/detectedmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/detectedpatterns(for:))*
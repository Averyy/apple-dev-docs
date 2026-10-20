# NSPasteboardItem.DetectedValues

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS 15.4+

## Declaration

```swift
typealias DetectedValues = NSPasteboard.DetectedValues
```

## See Also

### Detecting patterns and metadata in pasteboard items
- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>](./detectedpatterns%28for%29.md)
  Determines whether the pasteboard item matches the specified patterns, without notifying the person using the app.
- [func detectedValues(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> NSPasteboardItem.DetectedValues](./detectedvalues%28for%29.md)
  Determines whether this pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboardItem.DetectedMetadata>>) async throws -> NSPasteboardItem.DetectedMetadata](./detectedmetadata%28for%29.md)
  Determines available metadata from the specified metadata types for this pasteboard item, without notifying the person using the app.
- [NSPasteboardItem.DetectedMetadata](./detectedmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/detectedvalues)*
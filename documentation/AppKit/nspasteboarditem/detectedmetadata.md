# NSPasteboardItem.DetectedMetadata

**Framework**: AppKit  
**Kind**: typealias

**Availability**:
- macOS 15.4+

## Declaration

```swift
typealias DetectedMetadata = NSPasteboard.DetectedMetadata
```

## See Also

- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>](nspasteboarditem/detectedpatterns(for:).md)
  Determines whether the pasteboard item matches the specified patterns, without notifying the person using the app.
- [func detectedValues(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> NSPasteboardItem.DetectedValues](nspasteboarditem/detectedvalues(for:).md)
  Determines whether this pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [NSPasteboardItem.DetectedValues](nspasteboarditem/detectedvalues.md)
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboardItem.DetectedMetadata>>) async throws -> NSPasteboardItem.DetectedMetadata](nspasteboarditem/detectedmetadata(for:).md)
  Determines available metadata from the specified metadata types for this pasteboard item, without notifying the person using the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/detectedmetadata)*
# Pasteboard detection metadata types

**Framework**: AppKit

Common types of metadata that the data detection system matches for a pasteboard.

## Topics

### Accessing metadata
- [var metadataTypes: Set<PartialKeyPath<NSPasteboard.DetectedMetadata>>](nspasteboard/detectedmetadata/metadatatypes.md)
  A set of key paths that represent metadata types that the data detection system identifies.
- [var contentType: UTType?](nspasteboard/detectedmetadata/contenttype.md)
  The content type of a file that the data detection system identifies when the pasteboard contains a file URL.

## See Also

- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboard.DetectedValues>>](nspasteboard/detectedpatterns(for:).md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the person using the app.
- [func detectedValues(for: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> NSPasteboard.DetectedValues](nspasteboard/detectedvalues(for:).md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [NSPasteboard.DetectedValues](nspasteboard/detectedvalues.md)
  A type that contains common types of data that the data detection system matches for a pasteboard.
- [Pasteboard detection patterns](nspasteboard-detection-patterns.md)
  Common types of data that the data detection system matches for a pasteboard.
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboard.DetectedMetadata>>) async throws -> NSPasteboard.DetectedMetadata](nspasteboard/detectedmetadata(for:).md)
  Determines available metadata from the specified metadata types for the first pasteboard item, without notifying the person using the app.
- [NSPasteboard.DetectedMetadata](nspasteboard/detectedmetadata.md)
  An object that contains common types of metadata that the data detection system matches for a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard-detection-metadata-types)*
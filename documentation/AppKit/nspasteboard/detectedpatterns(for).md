# detectedPatterns(for:)

**Framework**: AppKit  
**Kind**: method

Determines whether the first pasteboard item matches the specified patterns, without notifying the person using the app.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func detectedPatterns(for keyPaths: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboard.DetectedValues>>
```

#### Return Value

A set with the patterns found on the pasteboard.

#### Discussion

This method only gives an indication of whether the first pasteboard item matches a particular pattern, and doesn’t allow the app to access the item’s contents. As a result, the system doesn’t notify the person using the app about reading the contents of the pasteboard.

The following example shows how to use this method to find calendar events in the first pasteboard item:

```swift
do {
    let patternResults = try await NSPasteboard.general.detectedPatterns(for: [\.calendarEvents])
    if patternResults.contains(\.calendarEvents) {
        print("Calendar event(s) detected.")
    } else {
        print("Didn't detect any calendar events.")
    }
} catch {
    print("Error: \(error).")
}
```

## Parameters

- `keyPaths`: The patterns to detect on the pasteboard.

## See Also

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
- [Pasteboard detection metadata types](nspasteboard-detection-metadata-types.md)
  Common types of metadata that the data detection system matches for a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/detectedpatterns(for:))*
# fileURL

**Framework**: App Intents  
**Kind**: property

A URL that locates a file saved to disk.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var fileURL: URL? { get async throws }
```

#### Discussion

If the file is saved outside of your app’s container, make sure to surround access to file contents with `startAccessingSecurityScopedResource()` and `stopAccessingSecurityScopedResource()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/fileentityidentifier/fileurl)*
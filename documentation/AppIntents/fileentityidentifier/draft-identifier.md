# draft(identifier:)

**Framework**: App Intents  
**Kind**: method

Creates and returns an identifier for a draft document.

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
static func draft(identifier: String) -> FileEntityIdentifier
```

#### Discussion

Only use this method to initialize identifiers for documents which aren’t materialized on disk yet and don’t have a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/fileentityidentifier/draft(identifier:))*
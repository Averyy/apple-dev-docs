# init(_:)

**Framework**: Evaluations  
**Kind**: init

Creates a partial argument matcher from the given generated content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
nonisolated
init(_ content: GeneratedContent) throws
```

#### Discussion

> **Note**: An error if the content doesn’t match a known matcher type.

## Parameters

- `content`: The generated content to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/partiallygenerated/init(_:))*
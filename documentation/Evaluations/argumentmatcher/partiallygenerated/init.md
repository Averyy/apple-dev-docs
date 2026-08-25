# init(_:)

**Framework**: Evaluations  
**Kind**: init

Creates a partial argument matcher from the given generated content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

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
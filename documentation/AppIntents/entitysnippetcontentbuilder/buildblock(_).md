# buildBlock(_:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Type Method

Creates a snippet from a single view declaration.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
static func buildBlock<C>(_ content: C) -> some EntitySnippetContent<Entity> where Entity == C.Entity, C : EntitySnippetContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitysnippetcontentbuilder/buildblock(_:))*
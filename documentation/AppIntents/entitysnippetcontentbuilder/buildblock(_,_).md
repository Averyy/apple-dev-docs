# buildBlock(_:_:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Type Method

Creates a snippet by combining two snippet declarations into a single representation.

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
static func buildBlock<C1, C2>(_ c1: C1, _ c2: C2) -> some EntitySnippetContent<Entity> where Entity == C1.Entity, C1 : EntitySnippetContent, C2 : EntitySnippetContent, C1.Entity == C2.Entity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitysnippetcontentbuilder/buildblock(_:_:))*
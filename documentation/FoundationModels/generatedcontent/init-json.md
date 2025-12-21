# init(json:)

**Framework**: Foundation Models  
**Kind**: init

Creates equivalent content from a JSON string.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(json: String) throws
```

#### Discussion

The JSON string you provide may be incomplete. This is useful for correctly handling partially generated responses.

```swift
@Generable struct NovelIdea {
  let title: String
}

let partial = #"{"title": "A story of"#
let content = try GeneratedContent(json: partial)
let idea = try NovelIdea(content)
print(idea.title) // A story of
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/init(json:))*
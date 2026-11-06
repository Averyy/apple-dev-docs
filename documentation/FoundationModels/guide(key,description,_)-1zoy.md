# Guide(key:description:_:)

**Framework**: Foundation Models  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@attached(peer)
macro Guide<T>(key: String, description: String? = nil, _ guides: GenerationGuide<T>...) where T : Generable
```

**Other overloads**:

```swift
@attached(peer)
macro Guide<RegexOutput>(key: String, description: String? = nil, _ guides: Regex<RegexOutput>)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/guide(key:description:_:)-1zoy)*
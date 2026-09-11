# init(url:)

**Framework**: Evaluations  
**Kind**: init

Creates a loader backed by the JSON or JSONL file at the given URL.

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
init(url: URL)
```

#### Discussion

```swift
var dataset: JSONLoader<ModelSample<String>> {
    let url = Bundle.main.url(forResource: "samples", withExtension: "jsonl")!
    return JSONLoader(url: url)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/jsonloader/init(url:))*
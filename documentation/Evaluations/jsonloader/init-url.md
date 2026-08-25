# init(url:)

**Framework**: Evaluations  
**Kind**: init

Creates a loader backed by the JSON or JSONL file at the given URL.

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
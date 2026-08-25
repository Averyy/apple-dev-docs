# init(stream:)

**Framework**: Evaluations  
**Kind**: init

Creates a loader backed by the given async sequence.

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
init(stream: some Sendable & AsyncSequence<Sample, any Error>)
```

#### Discussion

```swift
let loader = StreamLoader(stream: AsyncThrowingStream { continuation in
    continuation.yield(ModelSample(prompt: "What is 2+2?", expected: "4"))
    continuation.finish()
})
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/streamloader/init(stream:))*
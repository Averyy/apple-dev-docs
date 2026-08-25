# init(samples:)

**Framework**: Evaluations  
**Kind**: init

Creates a loader backed by the given array of samples.

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
init(samples: [Sample])
```

#### Discussion

```swift
let loader = ArrayLoader(samples: [
    ModelSample(prompt: "Is 7 a prime number?", expected: true),
])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/arrayloader/init(samples:))*
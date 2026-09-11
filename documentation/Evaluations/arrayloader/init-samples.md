# init(samples:)

**Framework**: Evaluations  
**Kind**: init

Creates a loader backed by the given array of samples.

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
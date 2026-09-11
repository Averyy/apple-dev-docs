# run()

**Framework**: Evaluations  
**Kind**: method

Runs the generator and returns a stream of newly synthesized samples.

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
nonisolated
func run() -> some AsyncSequence<SampleType, any Error>
```

#### Return Value

An async throwing stream of individual samples.

#### Discussion

Each element the stream yields is a newly generated sample. After iteration completes, access [`samples`](samplegenerator/samples.md) to retrieve the full dataset (initial + generated), or [`invalidSamples`](samplegenerator/invalidsamples.md) to see samples the validator rejected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/run())*
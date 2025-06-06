# receive(_:)

**Framework**: Combine  
**Kind**: method

Add an output to the recording.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
mutating func receive(_ input: Record<Output, Failure>.Recording.Input)
```

#### Discussion

A `fatalError` will be raised if output is added after adding completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/recording-swift.struct/receive(_:))*
# receive(completion:)

**Framework**: Combine  
**Kind**: method

Add a completion to the recording.

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
mutating func receive(completion: Subscribers.Completion<Failure>)
```

#### Discussion

A `fatalError` will be raised if more than one completion is added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/recording-swift.struct/receive(completion:))*
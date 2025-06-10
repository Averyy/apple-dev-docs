# next(isolation:)

**Framework**: Foundation Models  
**Kind**: method

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
mutating func next(isolation actor: isolated (any Actor)? = #isolation) async throws -> LanguageModelSession.ResponseStream<Content>.Element?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.

## See Also

- [LanguageModelSession.ResponseStream.AsyncIterator.Element](languagemodelsession/responsestream/asynciterator/element.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream/asynciterator/next(isolation:))*
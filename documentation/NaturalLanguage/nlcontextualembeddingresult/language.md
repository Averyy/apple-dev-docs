# language

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

The language that the framework identified or used when processing the input string.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var language: NLLanguage { get }
```

```objc
@property (copy, readonly) NLLanguage language;
```

## See Also

### Inspecting the result
- [var sequenceLength: Int](./sequencelength.md)
  The number of embedding vectors the request generates.
- [var string: String](./string.md)
  A copy of the input string used to generate the embedding vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingresult/language)*
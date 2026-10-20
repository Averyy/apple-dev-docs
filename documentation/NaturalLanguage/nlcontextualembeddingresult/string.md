# string

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

A copy of the input string used to generate the embedding vectors.

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
var string: String { get }
```

```objc
@property (copy, readonly) NSString * string;
```

## See Also

### Inspecting the result
- [var language: NLLanguage](./language.md)
  The language that the framework identified or used when processing the input string.
- [var sequenceLength: Int](./sequencelength.md)
  The number of embedding vectors the request generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingresult/string)*
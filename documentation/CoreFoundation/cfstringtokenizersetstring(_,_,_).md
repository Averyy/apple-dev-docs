# CFStringTokenizerSetString(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the string for a tokenizer.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFStringTokenizerSetString(_ tokenizer: CFStringTokenizer!, _ string: CFString!, _ range: CFRange)
```

## Parameters

- `tokenizer`: A tokenizer.
- `string`: The string for the tokenizer to tokenize.
- `range`: The range of string to tokenize. The range of characters within the string to be tokenized. The specified range must not exceed the length of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizersetstring(_:_:_:))*
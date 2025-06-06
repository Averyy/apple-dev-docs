# CFStringTokenizerGetCurrentTokenRange(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the range of the current token.

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
func CFStringTokenizerGetCurrentTokenRange(_ tokenizer: CFStringTokenizer!) -> CFRange
```

#### Return Value

The range of the current token, or `{``kCFNotFound`, `0}` if there is no current token.

## Parameters

- `tokenizer`: A CFStringTokenizer object.

## See Also

- [func CFStringTokenizerCopyCurrentTokenAttribute(CFStringTokenizer!, CFOptionFlags) -> CFTypeRef!](cfstringtokenizercopycurrenttokenattribute(_:_:).md)
  Returns a given attribute of the current token.
- [func CFStringTokenizerGetCurrentSubTokens(CFStringTokenizer!, UnsafeMutablePointer<CFRange>!, CFIndex, CFMutableArray!) -> CFIndex](cfstringtokenizergetcurrentsubtokens(_:_:_:_:).md)
  Retrieves the subtokens or derived subtokens contained in the compound token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizergetcurrenttokenrange(_:))*
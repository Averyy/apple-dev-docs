# CFStringTokenizerGetCurrentTokenRange(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern CFRange CFStringTokenizerGetCurrentTokenRange(CFStringTokenizerRef tokenizer);
```

#### Return Value

The range of the current token, or `{``kCFNotFound`, `0}` if there is no current token.

## Parameters

- `tokenizer`: A CFStringTokenizer object.

## See Also

### Getting Information About the Current Token
- [func CFStringTokenizerCopyCurrentTokenAttribute(CFStringTokenizer!, CFOptionFlags) -> CFTypeRef!](./cfstringtokenizercopycurrenttokenattribute%28_,_%29.md)
  Returns a given attribute of the current token.
- [func CFStringTokenizerGetCurrentSubTokens(CFStringTokenizer!, UnsafeMutablePointer<CFRange>!, CFIndex, CFMutableArray!) -> CFIndex](./cfstringtokenizergetcurrentsubtokens%28_,_,_,_%29.md)
  Retrieves the subtokens or derived subtokens contained in the compound token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizergetcurrenttokenrange(_:))*
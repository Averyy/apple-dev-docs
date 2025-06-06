# CFStringTokenizerCopyCurrentTokenAttribute(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a given attribute of the current token.

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
func CFStringTokenizerCopyCurrentTokenAttribute(_ tokenizer: CFStringTokenizer!, _ attribute: CFOptionFlags) -> CFTypeRef!
```

#### Return Value

The attribute specified by `attribute` of the current token, or `NULL` if the current token does not have the specified attribute or there is no current token. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `tokenizer`: A CFStringTokenizer object.
- `attribute`: The token attribute to obtain. The value must be  , or  .

## See Also

- [func CFStringTokenizerGetCurrentTokenRange(CFStringTokenizer!) -> CFRange](cfstringtokenizergetcurrenttokenrange(_:).md)
  Returns the range of the current token.
- [func CFStringTokenizerGetCurrentSubTokens(CFStringTokenizer!, UnsafeMutablePointer<CFRange>!, CFIndex, CFMutableArray!) -> CFIndex](cfstringtokenizergetcurrentsubtokens(_:_:_:_:).md)
  Retrieves the subtokens or derived subtokens contained in the compound token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizercopycurrenttokenattribute(_:_:))*
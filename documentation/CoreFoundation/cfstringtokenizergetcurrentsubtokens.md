# CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Retrieves the subtokens or derived subtokens contained in the compound token.

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
func CFStringTokenizerGetCurrentSubTokens(_ tokenizer: CFStringTokenizer!, _ ranges: UnsafeMutablePointer<CFRange>!, _ maxRangeLength: CFIndex, _ derivedSubTokens: CFMutableArray!) -> CFIndex
```

#### Return Value

The number of ranges returned.

#### Discussion

If token type is `kCFStringTokenizerTokenNone`, the `ranges` array and `derivedSubTokens` array are untouched and the return value is `0`.

If token type is `kCFStringTokenizerTokenNormal`, the `ranges` array has one item filled in with the entire range of the token (if `maxRangeLength` >= 1) and a string taken from the entire token range is added to the `derivedSubTokens` array and the return value is `1`.

If token type is `kCFStringTokenizerTokenHasSubTokensMask` or `kCFStringTokenizerTokenHasDerivedSubTokensMask`, the ranges array is filled in with as many items as there are subtokens (up to a limit of `maxRangeLength`).

The `derivedSubTokens` array will have sub tokens added even when the sub token is a substring of the token. If token type is `kCFStringTokenizerTokenHasSubTokensMask`, the ordinary non-derived subtokens are added to the `derivedSubTokens` array.

## Parameters

- `tokenizer`: A CFStringTokenizer object.
- `ranges`: Upon return, an array of CFRanges containing the ranges of subtokens. The ranges are relative to the string specified to CFStringTokenizerCreate. This parameter can be  .
- `maxRangeLength`: The maximum number of ranges to return.
- `derivedSubTokens`: A CFMutableArray to which the derived subtokens are to be added. This parameter can be  .

## See Also

- [func CFStringTokenizerCopyCurrentTokenAttribute(CFStringTokenizer!, CFOptionFlags) -> CFTypeRef!](cfstringtokenizercopycurrenttokenattribute(_:_:).md)
  Returns a given attribute of the current token.
- [func CFStringTokenizerGetCurrentTokenRange(CFStringTokenizer!) -> CFRange](cfstringtokenizergetcurrenttokenrange(_:).md)
  Returns the range of the current token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizergetcurrentsubtokens(_:_:_:_:))*
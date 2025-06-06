# NSGrammarRange

**Framework**: Foundation  
**Kind**: var

The value for the `NSGrammarRange` dictionary key should be an `NSValue` containing an `NSRange`, a subrange of the sentence range used as the return value, whose location should be an offset from the beginning of the sentence–so, for example, an `NSGrammarRange` for the first four characters of the overall sentence range should be `{0, 4}`. If the `NSGrammarRange` key is not present in the dictionary it is assumed to be equal to the overall sentence range.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let NSGrammarRange: String
```

## See Also

- [let NSGrammarUserDescription: String](nsgrammaruserdescription.md)
  The value for the `NSGrammarUserDescription` dictionary key should be an `NSString` containing descriptive text about that range, to be presented directly to the user; it is intended that the user description should provide enough information to allow the user to correct the problem. It is recommended that `NSGrammarUserDescription` be supplied in all cases, however, `NSGrammarUserDescription` or `NSGrammarCorrections` must be supplied in order for correction guidance to be presented to the user.
- [let NSGrammarCorrections: String](nsgrammarcorrections.md)
  The value for the `NSGrammarCorrections` key should be an `NSArray` of `NSStrings` representing potential substitutions to correct the problem, but it is expected that this may not be available in all cases. `NSGrammarUserDescription` or `NSGrammarCorrections` must be supplied in order for correction guidance to be presented to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgrammarrange)*
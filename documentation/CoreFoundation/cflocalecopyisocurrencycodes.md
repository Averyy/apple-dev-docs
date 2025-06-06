# CFLocaleCopyISOCurrencyCodes()

**Framework**: Core Foundation  
**Kind**: func

Returns an array of CFString objects that represents all known legal ISO currency codes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFLocaleCopyISOCurrencyCodes() -> CFArray!
```

#### Return Value

An array of CFString objects that represents all known legal ISO currency codes.Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Note: many of these will not have any supporting locale data in macOS.

## See Also

- [func CFLocaleCopyISOCountryCodes() -> CFArray!](cflocalecopyisocountrycodes().md)
  Returns an array of CFString objects that represents all known legal ISO country codes.
- [func CFLocaleCopyISOLanguageCodes() -> CFArray!](cflocalecopyisolanguagecodes().md)
  Returns an array of CFString objects that represents all known legal ISO language codes.
- [func CFLocaleCopyCommonISOCurrencyCodes() -> CFArray!](cflocalecopycommonisocurrencycodes().md)
  Returns an array of strings that represents ISO currency codes for currencies in common use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecopyisocurrencycodes())*
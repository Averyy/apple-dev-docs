# CFLocaleCopyCommonISOCurrencyCodes()

**Framework**: Core Foundation  
**Kind**: func

Returns an array of strings that represents ISO currency codes for currencies in common use.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFLocaleCopyCommonISOCurrencyCodes() -> CFArray!
```

#### Return Value

An array of CFString objects that represents ISO currency codes for currencies in common use. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

- [func CFLocaleCopyISOCountryCodes() -> CFArray!](cflocalecopyisocountrycodes().md)
  Returns an array of CFString objects that represents all known legal ISO country codes.
- [func CFLocaleCopyISOLanguageCodes() -> CFArray!](cflocalecopyisolanguagecodes().md)
  Returns an array of CFString objects that represents all known legal ISO language codes.
- [func CFLocaleCopyISOCurrencyCodes() -> CFArray!](cflocalecopyisocurrencycodes().md)
  Returns an array of CFString objects that represents all known legal ISO currency codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecopycommonisocurrencycodes())*
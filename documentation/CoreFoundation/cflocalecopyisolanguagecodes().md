# CFLocaleCopyISOLanguageCodes()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns an array of CFString objects that represents all known legal ISO language codes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFLocaleCopyISOLanguageCodes() -> CFArray!
```

```c
extern CFArrayRefCFLocaleCopyISOLanguageCodes();
```

#### Return Value

An array of CFString objects that represents all known legal ISO language codes. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Note: many of these will not have any supporting locale data in macOS.

## See Also

### Getting ISO Information
- [func CFLocaleCopyISOCountryCodes() -> CFArray!](./cflocalecopyisocountrycodes%28%29.md)
  Returns an array of CFString objects that represents all known legal ISO country codes.
- [func CFLocaleCopyISOCurrencyCodes() -> CFArray!](./cflocalecopyisocurrencycodes%28%29.md)
  Returns an array of CFString objects that represents all known legal ISO currency codes.
- [func CFLocaleCopyCommonISOCurrencyCodes() -> CFArray!](./cflocalecopycommonisocurrencycodes%28%29.md)
  Returns an array of strings that represents ISO currency codes for currencies in common use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecopyisolanguagecodes())*
# CFStringTokenizerCopyBestStringLanguage(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Guesses a language of a given string and returns the guess as a BCP 47 string.

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
func CFStringTokenizerCopyBestStringLanguage(_ string: CFString!, _ range: CFRange) -> CFString!
```

#### Return Value

A language in BCP 47 form, or `NULL` if the language in `string` could not be identified. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The result is not guaranteed to be accurate. Typically, the function requires 200-400 characters to reliably guess the language of a string.

CFStringTokenizer recognizes the following languages:

ar (Arabic), bg (Bulgarian), cs (Czech), da (Danish), de (German), el (Greek), en (English), es (Spanish), fi (Finnish), fr (French), he (Hebrew), hr (Croatian), hu (Hungarian), is (Icelandic), it (Italian), ja (Japanese), ko (Korean), nb (Norwegian Bokmål), nl (Dutch), pl (Polish), pt (Portuguese), ro (Romanian), ru (Russian), sk (Slovak), sv (Swedish), th (Thai), tr (Turkish), uk (Ukrainian), zh-Hans (Simplified Chinese), zh-Hant (Traditional Chinese).

## Parameters

- `string`: The string to test to identify the language.
- `range`: The range of   to use for the test. If  , the first few hundred characters of the string are examined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizercopybeststringlanguage(_:_:))*
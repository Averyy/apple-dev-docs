# CFLocaleGetLanguageCharacterDirection(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the character direction for the specified ISO language code.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFLocaleGetLanguageCharacterDirection(_ isoLangCode: CFString!) -> CFLocaleLanguageDirection
```

```c
extern CFLocaleLanguageDirection CFLocaleGetLanguageCharacterDirection(CFStringRef isoLangCode);
```

## Return Value

The character direction for the language. See [`CFLocaleLanguageDirection`](./cflocalelanguagedirection.md) for possible values. If the appropriate direction can’t be determined, [`CFLocaleLanguageDirection.unknown`](./cflocalelanguagedirection/unknown.md) is returned.

## Parameters

- `isoLangCode`: The ISO language code.

## See Also

### Getting Line and Character Direction for a Language
- [func CFLocaleGetLanguageLineDirection(CFString!) -> CFLocaleLanguageDirection](./cflocalegetlanguagelinedirection%28_%29.md)
  Returns the line direction for the specified ISO language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalegetlanguagecharacterdirection(_:))*
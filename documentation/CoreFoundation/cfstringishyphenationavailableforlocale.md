# CFStringIsHyphenationAvailableForLocale(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether hyphenation data is available.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFStringIsHyphenationAvailableForLocale(_ locale: CFLocale!) -> Bool
```

## Parameters

- `locale`: A valid locale that specifies which language’s hyphenation conventions to use. Hyphenation data is not available for all locales.

## See Also

- [func CFStringGetHyphenationLocationBeforeIndex(CFString!, CFIndex, CFRange, CFOptionFlags, CFLocale!, UnsafeMutablePointer<UTF32Char>!) -> CFIndex](cfstringgethyphenationlocationbeforeindex(_:_:_:_:_:_:).md)
  Retrieve the first potential hyphenation location found before the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringishyphenationavailableforlocale(_:))*
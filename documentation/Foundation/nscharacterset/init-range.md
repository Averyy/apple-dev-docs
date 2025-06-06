# init(range:)

**Framework**: Foundation  
**Kind**: init

Returns a character set containing characters with Unicode values in a given range.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(range aRange: NSRange)
```

#### Return Value

A character set containing characters whose Unicode values are given by `aRange`. If `aRange.length` is `0`, returns an empty character set.

#### Discussion

This code excerpt creates a character set object containing the lowercase English alphabetic characters:

```objc
NSRange lcEnglishRange;
NSCharacterSet *lcEnglishLetters;
 
lcEnglishRange.location = (unsigned int)'a';
lcEnglishRange.length = 26;
lcEnglishLetters = [NSCharacterSet characterSetWithRange:lcEnglishRange];
```

## Parameters

- `aRange`: A range of Unicode values.    is the value of the first character to return;   is the value of the last.

## See Also

- [init(coder: NSCoder)](nscharacterset/init(coder:).md)
- [init(charactersIn: String)](nscharacterset/init(charactersin:).md)
  Returns a character set containing the characters in a given string.
- [NSOpenStepUnicodeReservedBase](1560803-nsopenstepunicodereservedbase.md)
  Specifies lower bound for a Unicode character range reserved for Apple’s corporate use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/init(range:))*
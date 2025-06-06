# addCharacters(in:)

**Framework**: Foundation  
**Kind**: method

Adds to the receiver the characters whose Unicode values are in a given range.

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
func addCharacters(in aRange: NSRange)
```

#### Discussion

This code excerpt adds to a character set the lowercase English alphabetic characters:

```objc
NSMutableCharacterSet *aCharacterSet = [[NSMutableCharacterSet alloc] init];
NSRange lcEnglishRange;
 
lcEnglishRange.location = (unsigned int)'a';
lcEnglishRange.length = 26;
[aCharacterSet addCharactersInRange:lcEnglishRange];
```

## Parameters

- `aRange`: The range of characters to add.    is the value of the first character to add;   is the value of the last. If   is  , this method has no effect.

## See Also

- [String Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i)
- [func removeCharacters(in: NSRange)](nsmutablecharacterset/removecharacters(in:)-70nqp.md)
  Removes from the receiver the characters whose Unicode values are in a given range.
- [func addCharacters(in: String)](nsmutablecharacterset/addcharacters(in:)-7q02.md)
  Adds to the receiver the characters in a given string.
- [func removeCharacters(in: String)](nsmutablecharacterset/removecharacters(in:)-762gt.md)
  Removes from the receiver the characters in a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/addcharacters(in:)-4ppyw)*
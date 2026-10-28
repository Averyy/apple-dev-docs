# addCharacters(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addCharactersInRange:(NSRange) aRange;
```

## Discussion

This code excerpt adds to a character set the lowercase English alphabetic characters:

```objc
NSMutableCharacterSet *aCharacterSet = [[NSMutableCharacterSet alloc] init];
NSRange lcEnglishRange;
 
lcEnglishRange.location = (unsigned int)'a';
lcEnglishRange.length = 26;
[aCharacterSet addCharactersInRange:lcEnglishRange];
```

## Parameters

- `aRange`: The range of characters to add. `aRange.location` is the value of the first character to add; `aRange.location + aRange.length – 1` is the value of the last. If `aRange.length` is `0`, this method has no effect.

## See Also

### Related Documentation
- [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i)
### Adding and Removing Characters
- [func removeCharacters(in: NSRange)](./removecharacters%28in%29-70nqp.md)
  Removes from the receiver the characters whose Unicode values are in a given range.
- [func addCharacters(in: String)](./addcharacters%28in%29-7q02.md)
  Adds to the receiver the characters in a given string.
- [func removeCharacters(in: String)](./removecharacters%28in%29-762gt.md)
  Removes from the receiver the characters in a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/addcharacters(in:)-4ppyw)*
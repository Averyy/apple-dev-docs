# init(charactersIn:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a character set containing the characters in a given string.

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
init(charactersIn aString: String)
```

```objc
+ (NSCharacterSet *) characterSetWithCharactersInString:(NSString *) aString;
```

## Return Value

A character set containing the characters in `aString`. Returns an empty character set if `aString` is empty.

## Parameters

- `aString`: A string containing characters for the new character set.

## See Also

### Creating a Custom Character Set
- [init(coder: NSCoder)](./init%28coder%29.md)
- [init(range: NSRange)](./init%28range%29.md)
  Returns a character set containing characters with Unicode values in a given range.
- [NSOpenStepUnicodeReservedBase](../api-1560803-nsopenstepunicodereservedbase.md)
  Specifies lower bound for a Unicode character range reserved for Apple’s corporate use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/init(charactersin:))*
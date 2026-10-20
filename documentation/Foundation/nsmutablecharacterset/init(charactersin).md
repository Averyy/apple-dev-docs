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
+ (NSMutableCharacterSet *) characterSetWithCharactersInString:(NSString *) aString;
```

## See Also

### Creating Custom Character Sets
- [init(range: NSRange)](./init%28range%29.md)
  Returns a character set containing characters with Unicode values in a given range.
- [init(bitmapRepresentation: Data)](./init%28bitmaprepresentation%29.md)
  Returns a character set containing characters determined by a given bitmap representation.
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Returns a character set read from the bitmap representation stored in the file a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/init(charactersin:))*
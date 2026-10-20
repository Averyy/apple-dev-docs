# components(separatedBy:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array containing substrings from the receiver that have been divided by characters in a given set.

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
func components(separatedBy separator: CharacterSet) -> [String]
```

```objc
- (NSArray<NSString *> *) componentsSeparatedByCharactersInSet:(NSCharacterSet *) separator;
```

#### Return Value

An `NSArray` object containing substrings from the receiver that have been divided by characters in `separator`.

#### Discussion

The substrings in the array appear in the order they did in the receiver. Adjacent occurrences of the separator characters produce empty strings in the result. Similarly, if the string begins or ends with separator characters, the first or last substring, respectively, is empty.

## Parameters

- `separator`: A character set containing the characters to use to split the receiver. Must not be `nil`.

## See Also

### Dividing Strings
- [func components(separatedBy: String) -> [String]](./components%28separatedby%29-238fy.md)
  Returns an array containing substrings from the receiver that have been divided by a given separator.
- [func trimmingCharacters(in: CharacterSet) -> String](./trimmingcharacters%28in%29.md)
  Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [func substring(from: Int) -> String](./substring%28from%29.md)
  Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [func substring(with: NSRange) -> String](./substring%28with%29.md)
  Returns a string object containing the characters of the receiver that lie within a given range.
- [func substring(to: Int) -> String](./substring%28to%29.md)
  Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/components(separatedby:)-27x9g)*
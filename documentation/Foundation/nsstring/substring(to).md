# substring(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.

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
func substring(to: Int) -> String
```

```objc
- (NSString *) substringToIndex:(NSUInteger) to;
```

#### Return Value

A new string containing the characters of the receiver up to, but not including, the one at `anIndex`. If `anIndex` is equal to the length of the string, returns a copy of the receiver.

## Parameters

- `to`: An index. The value must lie within the bounds of the receiver, or be equal to the length of the receiver.

  Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if (`anIndex` - 1) lies beyond the end of the receiver.

## See Also

### Dividing Strings
- [func components(separatedBy: String) -> [String]](./components%28separatedby%29-238fy.md)
  Returns an array containing substrings from the receiver that have been divided by a given separator.
- [func components(separatedBy: CharacterSet) -> [String]](./components%28separatedby%29-27x9g.md)
  Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [func trimmingCharacters(in: CharacterSet) -> String](./trimmingcharacters%28in%29.md)
  Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [func substring(from: Int) -> String](./substring%28from%29.md)
  Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [func substring(with: NSRange) -> String](./substring%28with%29.md)
  Returns a string object containing the characters of the receiver that lie within a given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/substring(to:))*
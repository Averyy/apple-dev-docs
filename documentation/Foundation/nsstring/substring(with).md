# substring(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a string object containing the characters of the receiver that lie within a given range.

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
func substring(with range: NSRange) -> String
```

```objc
- (NSString *) substringWithRange:(NSRange) range;
```

## Return Value

A string object containing the characters of the receiver that lie within `aRange`.

## Discussion

This method detects all invalid ranges (including those with negative lengths). For applications linked against macOS 10.6 and later, this error causes an exception; for applications linked against earlier releases, this error causes a warning, which is displayed just once per application execution.

## Parameters

- `range`: A range. The range must not exceed the bounds of the receiver.

  Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if (`aRange.location` - 1) or (`aRange.location` + `aRange.length` - 1) lies beyond the end of the receiver.

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
- [func substring(to: Int) -> String](./substring%28to%29.md)
  Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/substring(with:))*
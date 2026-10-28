# appendFormat:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a constructed string to the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) appendFormat:(NSString *) format;
```

## Discussion

Pass a comma-separated list of trailing variadic arguments to substitute into `format`.

## Parameters

- `format`: A format string. See [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943) for more information. This value must not be `nil`.

  > ❗ **Important**:  Raises an `NSInvalidArgumentException` if `format` is `nil`.

## See Also

### Modifying a String
- [func append(String)](./append%28_%29.md)
  Adds to the end of the receiver the characters of a given string.
- [func applyTransform(StringTransform, reverse: Bool, range: NSRange, updatedRange: NSRangePointer?) -> Bool](./applytransform%28_,reverse,range,updatedrange%29.md)
  Transliterates the receiver by applying a specified ICU string transform.
- [func deleteCharacters(in: NSRange)](./deletecharacters%28in%29.md)
  Removes from the receiver the characters in a given range.
- [func insert(String, at: Int)](./insert%28_,at%29.md)
  Inserts into the receiver the characters of a given string at a given location.
- [func replaceCharacters(in: NSRange, with: String)](./replacecharacters%28in,with%29.md)
  Replaces the characters from `range` with those in `aString`.
- [func replaceOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> Int](./replaceoccurrences%28of,with,options,range%29.md)
  Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [func setString(String)](./setstring%28_%29.md)
  Replaces the characters of the receiver with those in a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring/appendformat:)*
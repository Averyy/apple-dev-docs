# setString(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the characters of the receiver with those in a given string.

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
func setString(_ aString: String)
```

```objc
- (void) setString:(NSString *) aString;
```

## Parameters

- `aString`: The string with which to replace the receiver’s content. `aString` must not be `nil`.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring/setstring(_:))*
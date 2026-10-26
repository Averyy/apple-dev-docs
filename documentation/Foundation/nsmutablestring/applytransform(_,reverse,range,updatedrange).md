# applyTransform(_:reverse:range:updatedRange:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Transliterates the receiver by applying a specified ICU string transform.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func applyTransform(_ transform: StringTransform, reverse: Bool, range: NSRange, updatedRange resultingRange: NSRangePointer?) -> Bool
```

```objc
- (BOOL) applyTransform:(NSStringTransform) transform reverse:(BOOL) reverse range:(NSRange) range updatedRange:(NSRangePointer) resultingRange;
```

#### Return Value

[`true`](../../Swift/true.md) if the transform was successfully applied. Otherwise, [`false`](../../Swift/false.md).

#### Discussion

In addition to the provided transformation constants, you may use any valid ICU transform ID as defined in the [ICU User Guide](http://userguide.icu-project.org/transforms/general). However, arbitrary ICU transform rules are not supported.

## Parameters

- `transform`: The transformation to apply. For a list of possible values, see [String Transformations](../string-transformations.md). If the specified transform does not exist, the receiver is not modified, and this method returns [`false`](../../Swift/false.md).
- `reverse`: Whether an inverse transform should be used. If the specified transform does not have an inverse, the receiver is not modified, and this method returns [`false`](../../Swift/false.md).
- `range`: The range of the string to transform. `range` must not exceed the bounds of the receiver.

  > ❗ **Important**:  Raises an `NSRangeException` if any part of `aRange` lies beyond the end of the string.
- `resultingRange`: If the transform was successfully applied, upon return contains the range of the transformed string.

## See Also

### Modifying a String
- [func append(String)](./append%28_%29.md)
  Adds to the end of the receiver the characters of a given string.
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
- [- appendFormat:](./appendformat_.md)
  Adds a constructed string to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring/applytransform(_:reverse:range:updatedrange:))*
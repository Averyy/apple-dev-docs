# applyTransform(_:reverse:range:updatedRange:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the transform was successfully applied. Otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

In addition to the provided transformation constants, you may use any valid ICU transform ID as defined in the [`ICU User Guide`](https://developer.apple.comhttp://userguide.icu-project.org/transforms/general). However, arbitrary ICU transform rules are not supported.

## Parameters

- `transform`: The transformation to apply. For a list of possible values, see  . If the specified transform does not exist, the receiver is not modified, and this method returns  .
- `reverse`: Whether an inverse transform should be used. If the specified transform does not have an inverse, the receiver is not modified, and this method returns  .
- `range`: The range of the string to transform.   must not exceed the bounds of the receiver.
- `resultingRange`: If the transform was successfully applied, upon return contains the range of the transformed string.

## See Also

- [func append(String)](nsmutablestring/append(_:).md)
  Adds to the end of the receiver the characters of a given string.
- [func deleteCharacters(in: NSRange)](nsmutablestring/deletecharacters(in:).md)
  Removes from the receiver the characters in a given range.
- [func insert(String, at: Int)](nsmutablestring/insert(_:at:).md)
  Inserts into the receiver the characters of a given string at a given location.
- [func replaceCharacters(in: NSRange, with: String)](nsmutablestring/replacecharacters(in:with:).md)
  Replaces the characters from `range` with those in `aString`.
- [func replaceOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> Int](nsmutablestring/replaceoccurrences(of:with:options:range:).md)
  Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [func setString(String)](nsmutablestring/setstring(_:).md)
  Replaces the characters of the receiver with those in a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring/applytransform(_:reverse:range:updatedrange:))*
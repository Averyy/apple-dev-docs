# applyingTransform(_:reverse:)

**Framework**: Foundation  
**Kind**: method

Returns a new string by applying a specified transform to the string.

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
func applyingTransform(_ transform: StringTransform, reverse: Bool) -> String?
```

#### Discussion

You can use this method to, for example, transliterate text from one script to another, strip diacritics or combining marks, and get the unicode names of characters.

> **Note**:  The constants defined by the [`StringTransform`](stringtransform.md) type offer a subset of the functionality provided by the underlying ICU transform functionality. To apply an ICU transform defined in the [`ICU User Guide`](https://developer.apple.comhttp://userguide.icu-project.org/transforms/general) that doesn’t have a corresponding [`StringTransform`](stringtransform.md) constant, create an instance of  [`NSMutableString`](nsmutablestring.md) and call the [`applyTransform(_:reverse:range:updatedRange:)`](nsmutablestring/applytransform(_:reverse:range:updatedrange:).md) method instead.

.

## See Also

- [func applyTransform(StringTransform, reverse: Bool, range: NSRange, updatedRange: NSRangePointer?) -> Bool](nsmutablestring/applytransform(_:reverse:range:updatedrange:).md)
  Transliterates the receiver by applying a specified ICU string transform.
- [struct StringTransform](stringtransform.md)
  Constants representing an ICU string transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/applyingtransform(_:reverse:))*
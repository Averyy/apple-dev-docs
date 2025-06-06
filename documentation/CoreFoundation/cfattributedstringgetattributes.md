# CFAttributedStringGetAttributes(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the attributes of an attributed string at a specified location.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFAttributedStringGetAttributes(_ aStr: CFAttributedString!, _ loc: CFIndex, _ effectiveRange: UnsafeMutablePointer<CFRange>!) -> CFDictionary!
```

#### Return Value

A dictionary that contains the attributes of `str` at the specified location. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

For performance reasons, a range returned in `effectiveRange` is not necessarily the maximal range. If you need the maximum range, you should use [`CFAttributedStringGetAttributesAndLongestEffectiveRange(_:_:_:_:)`](cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:).md).

Note that the returned attribute dictionary might change in unpredictable ways if the attributed string is edited after this call. If you want to preserve the state of the dictionary, you should make an actual copy of it rather than just retaining it. In addition, you should make no assumptions about the relationship of the actual dictionary returned by this call and the dictionary originally used to set the attributes, other than the fact that the values stored in the dictionaries will be identical (that is, `==`) to those originally specified.

## Parameters

- `aStr`: The attributed string to examine.
- `loc`: The location in   at which to determine the attributes.   must not exceed the bounds of  .
- `effectiveRange`: If not  , upon return contains a range including   over which exactly the same set of attributes apply as at  .

## See Also

- [func CFAttributedStringGetAttribute(CFAttributedString!, CFIndex, CFString!, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](cfattributedstringgetattribute(_:_:_:_:).md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributeAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFString!, CFRange, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](cfattributedstringgetattributeandlongesteffectiverange(_:_:_:_:_:).md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributesAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFRange, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:).md)
  Returns the attributes of an attributed string at a specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetattributes(_:_:_:))*
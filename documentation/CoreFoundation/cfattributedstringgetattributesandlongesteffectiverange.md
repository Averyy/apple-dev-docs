# CFAttributedStringGetAttributesAndLongestEffectiveRange(_:_:_:_:)

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
func CFAttributedStringGetAttributesAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>!) -> CFDictionary!
```

#### Return Value

A dictionary that contains the attributes of `str` at the specified location. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `aStr`: The attributed string to examine.
- `loc`: The location in   at which to determine the attributes.   must not exceed the bounds of  .
- `inRange`: The range in   within to find the longest effective range of the attributes at  .   must not exceed the bounds of  .
- `longestEffectiveRange`: If  not  , upon return contains the maximal range within   over which the exact same set of attributes apply. The returned range is clipped to  .

## See Also

- [func CFAttributedStringGetAttribute(CFAttributedString!, CFIndex, CFString!, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](cfattributedstringgetattribute(_:_:_:_:).md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributes(CFAttributedString!, CFIndex, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](cfattributedstringgetattributes(_:_:_:).md)
  Returns the attributes of an attributed string at a specified location.
- [func CFAttributedStringGetAttributeAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFString!, CFRange, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](cfattributedstringgetattributeandlongesteffectiverange(_:_:_:_:_:).md)
  Returns the value of a given attribute of an attributed string at a specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:))*
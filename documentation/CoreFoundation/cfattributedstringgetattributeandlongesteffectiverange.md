# CFAttributedStringGetAttributeAndLongestEffectiveRange(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the value of a given attribute of an attributed string at a specified location.

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
func CFAttributedStringGetAttributeAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>!) -> CFTypeRef!
```

#### Return Value

A dictionary that contains the attributes of `str` at the specified location. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `aStr`: The attributed string to examine.
- `loc`: The location in   at which to determine the attributes. It is a programming error for   to specify a location outside the bounds of  .
- `attrName`: The name of the attribute whose value you want to determine.
- `inRange`: The range in   within which you want to find the longest effective range of the attributes at  .   must not exceed the bounds of  .
- `longestEffectiveRange`: If not  , upon return contains the maximal range within   over which the exact same set of attributes apply. The returned range is clipped to  .

## See Also

- [func CFAttributedStringGetAttribute(CFAttributedString!, CFIndex, CFString!, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](cfattributedstringgetattribute(_:_:_:_:).md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributes(CFAttributedString!, CFIndex, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](cfattributedstringgetattributes(_:_:_:).md)
  Returns the attributes of an attributed string at a specified location.
- [func CFAttributedStringGetAttributesAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFRange, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:).md)
  Returns the attributes of an attributed string at a specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetattributeandlongesteffectiverange(_:_:_:_:_:))*
# CFAttributedStringGetAttributesAndLongestEffectiveRange(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the attributes of an attributed string at a specified location.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFAttributedStringGetAttributesAndLongestEffectiveRange(_ aStr: CFAttributedString!, _ loc: CFIndex, _ inRange: CFRange, _ longestEffectiveRange: UnsafeMutablePointer<CFRange>!) -> CFDictionary!
```

```c
extern CFDictionaryRefCFAttributedStringGetAttributesAndLongestEffectiveRange(CFAttributedStringRef aStr, CFIndex loc, CFRange inRange, CFRange *longestEffectiveRange);
```

#### Return Value

A dictionary that contains the attributes of `str` at the specified location. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `aStr`: The attributed string to examine.
- `loc`: The location in `str` at which to determine the attributes. `loc` must not exceed the bounds of `str`.
- `inRange`: The range in `str` within to find the longest effective range of the attributes at `loc`. `inRange` must not exceed the bounds of `str`.
- `longestEffectiveRange`: If  not `NULL`, upon return contains the maximal range within `inRange` over which the exact same set of attributes apply. The returned range is clipped to `inRange`.

## See Also

### Accessing Attributes
- [func CFAttributedStringGetAttribute(CFAttributedString!, CFIndex, CFString!, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](./cfattributedstringgetattribute%28_,_,_,_%29.md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributes(CFAttributedString!, CFIndex, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](./cfattributedstringgetattributes%28_,_,_%29.md)
  Returns the attributes of an attributed string at a specified location.
- [func CFAttributedStringGetAttributeAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFString!, CFRange, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](./cfattributedstringgetattributeandlongesteffectiverange%28_,_,_,_,_%29.md)
  Returns the value of a given attribute of an attributed string at a specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:))*
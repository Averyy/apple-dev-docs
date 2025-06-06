# CFAttributedStringGetAttribute(_:_:_:_:)

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
func CFAttributedStringGetAttribute(_ aStr: CFAttributedString!, _ loc: CFIndex, _ attrName: CFString!, _ effectiveRange: UnsafeMutablePointer<CFRange>!) -> CFTypeRef!
```

#### Return Value

The value of the specified attribute at the specified location in `str`. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

For performance reasons, a range returned in `effectiveRange` is not necessarily the maximal range. If you need the maximum range, you should use [`CFAttributedStringGetAttributeAndLongestEffectiveRange(_:_:_:_:_:)`](cfattributedstringgetattributeandlongesteffectiverange(_:_:_:_:_:).md).

## Parameters

- `aStr`: The attributed string to examine.
- `loc`: The location in   at which to determine the attributes.   must not exceed the bounds of  .
- `attrName`: The name of the attribute whose value you want to determine.
- `effectiveRange`: If not  , upon return contains a range including   over which exactly the same set of attributes apply as at  .

## See Also

- [func CFAttributedStringGetAttributes(CFAttributedString!, CFIndex, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](cfattributedstringgetattributes(_:_:_:).md)
  Returns the attributes of an attributed string at a specified location.
- [func CFAttributedStringGetAttributeAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFString!, CFRange, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](cfattributedstringgetattributeandlongesteffectiverange(_:_:_:_:_:).md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributesAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFRange, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:).md)
  Returns the attributes of an attributed string at a specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetattribute(_:_:_:_:))*
# CTFontDescriptorCopyAttributes(_:)

**Framework**: Core Text  
**Kind**: func

Returns the attributes dictionary of the font descriptor.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontDescriptorCopyAttributes(_ descriptor: CTFontDescriptor) -> CFDictionary
```

#### Return Value

The font descriptor attributes dictionary. This dictionary contains the minimum number of attributes to specify fully this particular font descriptor.

## Parameters

- `descriptor`: The font descriptor.

## See Also

- [func CTFontDescriptorCopyAttribute(CTFontDescriptor, CFString) -> CFTypeRef?](ctfontdescriptorcopyattribute(_:_:).md)
  Returns the value associated with an arbitrary attribute.
- [func CTFontDescriptorCopyLocalizedAttribute(CTFontDescriptor, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFTypeRef?](ctfontdescriptorcopylocalizedattribute(_:_:_:).md)
  Returns a localized value for the requested attribute, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcopyattributes(_:))*
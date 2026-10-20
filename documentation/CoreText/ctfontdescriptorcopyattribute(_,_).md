# CTFontDescriptorCopyAttribute(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the value associated with an arbitrary attribute.

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
func CTFontDescriptorCopyAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString) -> CFTypeRef?
```

```c
extern CFTypeRefCTFontDescriptorCopyAttribute(CTFontDescriptorRef descriptor, CFStringRef attribute);
```

#### Return Value

A retained reference to an arbitrary attribute, or `NULL` if the requested attribute is not present.

#### Discussion

Refer to Accessing Font Attributes for documentation explaining how each attribute is packaged as a CFType object.

## Parameters

- `descriptor`: The font descriptor.
- `attribute`: The requested attribute.

## See Also

### Getting Attributes
- [func CTFontDescriptorCopyAttributes(CTFontDescriptor) -> CFDictionary](./ctfontdescriptorcopyattributes%28_%29.md)
  Returns the attributes dictionary of the font descriptor.
- [func CTFontDescriptorCopyLocalizedAttribute(CTFontDescriptor, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFTypeRef?](./ctfontdescriptorcopylocalizedattribute%28_,_,_%29.md)
  Returns a localized value for the requested attribute, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcopyattribute(_:_:))*
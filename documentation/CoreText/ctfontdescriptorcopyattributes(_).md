# CTFontDescriptorCopyAttributes(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

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

```c
extern CFDictionaryRefCTFontDescriptorCopyAttributes(CTFontDescriptorRef descriptor);
```

#### Return Value

The font descriptor attributes dictionary. This dictionary contains the minimum number of attributes to specify fully this particular font descriptor.

## Parameters

- `descriptor`: The font descriptor.

## See Also

### Getting Attributes
- [func CTFontDescriptorCopyAttribute(CTFontDescriptor, CFString) -> CFTypeRef?](./ctfontdescriptorcopyattribute%28_,_%29.md)
  Returns the value associated with an arbitrary attribute.
- [func CTFontDescriptorCopyLocalizedAttribute(CTFontDescriptor, CFString, UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFTypeRef?](./ctfontdescriptorcopylocalizedattribute%28_,_,_%29.md)
  Returns a localized value for the requested attribute, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcopyattributes(_:))*
# MTCopyLocalizedNameForMediaSubType(_:_:)

**Framework**: Media Toolbox  
**Kind**: func  
**Role**: Function

Returns a localized name for the specified media type and subtype.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MTCopyLocalizedNameForMediaSubType(_ mediaType: CMMediaType, _ mediaSubType: FourCharCode) -> CFString?
```

```c
extern CFStringRefMTCopyLocalizedNameForMediaSubType(CMMediaType mediaType, FourCharCode mediaSubType);
```

## See Also

### Utility
- [func MTCopyLocalizedNameForMediaType(CMMediaType) -> CFString?](./mtcopylocalizednameformediatype%28_%29.md)
  Returns a localized name for the specified media type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtcopylocalizednameformediasubtype(_:_:))*
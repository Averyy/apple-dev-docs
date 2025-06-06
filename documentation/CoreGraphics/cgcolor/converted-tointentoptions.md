# converted(to:intent:options:)

**Framework**: Core Graphics  
**Kind**: method

Creates a new color in a different color space that matches the provided color.

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
func converted(to _: CGColorSpace, intent: CGColorRenderingIntent, options: CFDictionary?) -> CGColor?
```

##### Parameters

##### Returns

A new color in the destination color space that matches (or closely approximates) the source color.

#### Discussion

To create the new color, this method creates a `CFColorConverterRef` using the options you specified and applies it to the source color.

## See Also

- [class let conversionTRCSize: CFString](cgcolor/conversiontrcsize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor/converted(to:intent:options:))*
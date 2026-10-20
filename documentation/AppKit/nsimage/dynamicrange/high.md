# NSImage.DynamicRange.high

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Allows image content to use extended dynamic range if it has dynamic range content.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case high
```

```c
NSImageDynamicRangeHigh
```

## See Also

### Setting the dynamic range
- [NSImage.DynamicRange.standard](./standard.md)
  Restricts the image content dynamic range to the standard range regardless of the actual range of the image content.
- [NSImage.DynamicRange.constrainedHigh](./constrainedhigh.md)
  Allows for constrained High Dynamic Range (HDR) image content which is useful for mixing HDR and Standard Dynamic Range (SDR) content.
- [NSImage.DynamicRange.unspecified](./unspecified.md)
  Indicates that the dynamic range treatment of the image is unknown or otherwise unspecified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/dynamicrange/high)*
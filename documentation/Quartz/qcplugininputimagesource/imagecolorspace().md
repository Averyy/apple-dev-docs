# imageColorSpace()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the color space of the image source.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func imageColorSpace() -> Unmanaged<CGColorSpace>!
```

```objc
- (CGColorSpaceRef) imageColorSpace;
```

#### Return Value

The color space of the image source, typically RGB or Gray type.

## See Also

### Getting Color Space Information
- [func shouldColorMatch() -> Bool](./shouldcolormatch%28%29.md)
  Returns whether or not the image source should be color matched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/imagecolorspace())*
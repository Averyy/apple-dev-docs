# colorSpace()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the color space used by the rendering context.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func colorSpace() -> Unmanaged<CGColorSpace>!
```

```objc
- (CGColorSpaceRef) colorSpace;
```

## Return Value

An RGB color space; `NULL` if the custom patch execution mode is not consumer.

## Discussion

If the method returns a color space, it must be an RGB color space.

## See Also

### Getting Execution Context Information
- [func userInfo() -> NSMutableDictionary!](./userinfo%28%29.md)
  Returns a mutable dictionary that contains information that can be shared between all instances of the `QCPlugIn` subclass, running in the same Quartz Composer context.
- [func bounds() -> NSRect](./bounds%28%29.md)
  Returns the bounds of the rendering context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/colorspace())*
# bounds()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the bounds of the rendering context.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func bounds() -> NSRect
```

```objc
- (NSRect) bounds;
```

## Return Value

The bounds of the rendering context expressed in Quartz Composer units.

## See Also

### Getting Execution Context Information
- [func userInfo() -> NSMutableDictionary!](./userinfo%28%29.md)
  Returns a mutable dictionary that contains information that can be shared between all instances of the `QCPlugIn` subclass, running in the same Quartz Composer context.
- [func colorSpace() -> Unmanaged<CGColorSpace>!](./colorspace%28%29.md)
  Returns the color space used by the rendering context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/bounds())*
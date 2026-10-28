# shouldColorMatch()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns whether or not the image source should be color matched.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func shouldColorMatch() -> Bool
```

```objc
- (BOOL) shouldColorMatch;
```

## Return Value

[`false`](../../Swift/false.md) if the source is a mask or gradient; [`true`](../../Swift/true.md) otherwise.

## See Also

### Getting Color Space Information
- [func imageColorSpace() -> Unmanaged<CGColorSpace>!](./imagecolorspace%28%29.md)
  Returns the color space of the image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource/shouldcolormatch())*
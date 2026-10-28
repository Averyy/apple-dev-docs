# userInfo()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a mutable dictionary that contains information that can be shared between all instances of the `QCPlugIn` subclass, running in the same Quartz Composer context.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func userInfo() -> NSMutableDictionary!
```

```objc
- (NSMutableDictionary *) userInfo;
```

## Return Value

A mutable dictionary.

## Discussion

When you add information to the dictionary, make sure that you use unique keys, such as `com.myCompany.foo`. You can use this dictionary to cache data that you want to share.

## See Also

### Getting Execution Context Information
- [func bounds() -> NSRect](./bounds%28%29.md)
  Returns the bounds of the rendering context.
- [func colorSpace() -> Unmanaged<CGColorSpace>!](./colorspace%28%29.md)
  Returns the color space used by the rendering context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext/userinfo())*
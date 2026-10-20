# eraseColor()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Retrieves the current color used to erase the view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func eraseColor() -> NSColor!
```

```objc
- (NSColor *) eraseColor;
```

#### Return Value

The color object previously set using the [`setEraseColor(_:)`](./seterasecolor%28_%29.md) method.

## See Also

### Managing the Erase Color
- [func erase()](./erase%28%29.md)
  Clears the view using the current erase color.
- [func setEraseColor(NSColor!)](./seterasecolor%28_%29.md)
  Sets the color used to erase the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/erasecolor())*
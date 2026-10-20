# setEraseColor(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the color used to erase the view.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setEraseColor(_ color: NSColor!)
```

```objc
- (void) setEraseColor:(NSColor *) color;
```

## Parameters

- `color`: A color object.

## See Also

### Managing the Erase Color
- [func erase()](./erase%28%29.md)
  Clears the view using the current erase color.
- [func eraseColor() -> NSColor!](./erasecolor%28%29.md)
  Retrieves the current color used to erase the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/seterasecolor(_:))*
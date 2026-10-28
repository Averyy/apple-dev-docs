# refreshRate

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property

The mode’s refresh rate.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var refreshRate: Double { get }
```

```objc
@property (nonatomic, readonly) double refreshRate;
```

## Discussion

Consider supplying only modes that have a refresh rate equal to that of the host environment’s physical display.

## See Also

### Inspecting Mode Properties
- [var sizeInPixels: PGDisplayCoord_t](./sizeinpixels.md)
  The display mode’s dimensions in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaymode/refreshrate)*
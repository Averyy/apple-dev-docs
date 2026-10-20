# init(sizeInPixels:refreshRateInHz:)

**Framework**: Paravirtualized Graphics  
**Kind**: init  
**Role**: Initializer

Creates a new display mode.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
init?(sizeInPixels: PGDisplayCoord_t, refreshRateInHz: Double)
```

```objc
- (PGDisplayMode *) initWithSizeInPixels:(PGDisplayCoord_t) sizeInPixels refreshRateInHz:(double) refreshRateInHz;
```

## Parameters

- `sizeInPixels`: The display mode’s dimensions in pixels.
- `refreshRateInHz`: The mode’s refresh rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaymode/init(sizeinpixels:refreshrateinhz:))*
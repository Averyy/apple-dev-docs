# oldestLast

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

Particles are rendered oldest last. This mode uses source-over compositing.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let oldestLast: CAEmitterLayerRenderMode
```

```c
extern CAEmitterLayerRenderMode const kCAEmitterLayerOldestLast;
```

## See Also

### Constants
- [static let unordered: CAEmitterLayerRenderMode](./unordered.md)
  Particles are rendered unordered. This mode uses source-over compositing.
- [static let oldestFirst: CAEmitterLayerRenderMode](./oldestfirst.md)
  Particles are rendered oldest first. This mode uses source-over compositing.
- [static let backToFront: CAEmitterLayerRenderMode](./backtofront.md)
  Particles are rendered from back to front, sorted by z-position. This mode uses source-over compositing.
- [static let additive: CAEmitterLayerRenderMode](./additive.md)
  The particles are rendered using source-additive compositing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayerrendermode/oldestlast)*
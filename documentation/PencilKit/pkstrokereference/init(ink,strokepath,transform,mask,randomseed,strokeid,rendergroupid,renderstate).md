# init(ink:strokePath:transform:mask:randomSeed:strokeID:renderGroupID:renderState:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32, strokeID: UUID, renderGroupID: UUID?, renderState: PKStrokeRenderStateReference?)
```

*macOS*

```swift
init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?, randomSeed: UInt32, strokeID: UUID, renderGroupID: UUID?, renderState: PKStrokeRenderStateReference?)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (instancetype) initWithInk:(PKInk *) ink strokePath:(PKStrokePath *) strokePath transform:(CGAffineTransform) transform mask:(UIBezierPath *) mask randomSeed:(uint32_t) randomSeed strokeID:(NSUUID *) strokeID renderGroupID:(NSUUID *) renderGroupID renderState:(PKStrokeRenderState *) renderState;
```

*macOS*

```objc
- (instancetype) initWithInk:(PKInk *) ink strokePath:(PKStrokePath *) strokePath transform:(CGAffineTransform) transform mask:(NSBezierPath *) mask randomSeed:(uint32_t) randomSeed strokeID:(NSUUID *) strokeID renderGroupID:(NSUUID *) renderGroupID renderState:(PKStrokeRenderState *) renderState;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/init(ink:strokepath:transform:mask:randomseed:strokeid:rendergroupid:renderstate:))*
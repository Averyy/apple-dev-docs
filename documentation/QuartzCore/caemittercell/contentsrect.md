# contentsRect

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A rectangle (in the unit coordinate space) that specifies the portion of [`contents`](./contents.md) that the receiver should draw. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var contentsRect: CGRect { get set }
```

```objc
@property CGRect contentsRect;
```

#### Discussion

By default, this property is set to the unit rectangle (0.0,0.0,1.0,1.0), which results in all of the layer’s contents being drawn.

If pixels outside the unit rectangle are requested, the edge pixels of the contents image are extended outwards.

If you assign an empty rectangle to this property, the results are undefined.

## See Also

### Providing Emitter Cell Content
- [var contents: Any?](./contents.md)
  An object that provides the contents of the layer. Animatable.
- [var emitterCells: [CAEmitterCell]?](./emittercells.md)
  An optional array containing the sub-cells of this cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/contentsrect)*
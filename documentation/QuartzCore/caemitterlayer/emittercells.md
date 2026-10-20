# emitterCells

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The array emitter cells attached to the layer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emitterCells: [CAEmitterCell]? { get set }
```

```objc
@property (copy, nullable) NSArray<CAEmitterCell *> * emitterCells;
```

#### Discussion

Each object in the array must be an instance of the `CAEmitterCell` class.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/emittercells)*
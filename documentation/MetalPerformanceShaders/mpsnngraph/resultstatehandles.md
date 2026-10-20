# resultStateHandles

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var resultStateHandles: [any MPSHandle]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<id<MPSHandle>> * resultStateHandles;
```

## See Also

### Instance Properties
- [var destinationImageAllocator: any MPSImageAllocator](./destinationimageallocator.md)
- [protocol MPSImageAllocator](../mpsimageallocator.md)
- [var intermediateImageHandles: [any MPSHandle]?](./intermediateimagehandles.md)
- [var outputStateIsTemporary: Bool](./outputstateistemporary.md)
- [var resultHandle: (any MPSHandle)?](./resulthandle.md)
- [var sourceImageHandles: [any MPSHandle]](./sourceimagehandles.md)
- [var sourceStateHandles: [any MPSHandle]?](./sourcestatehandles.md)
- [var format: MPSImageFeatureChannelFormat](./format.md)
- [var resultImageIsNeeded: Bool](./resultimageisneeded.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph/resultstatehandles)*
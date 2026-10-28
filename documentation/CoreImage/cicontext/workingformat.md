# workingFormat

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The working pixel format of the Core Image context.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var workingFormat: CIFormat { get }
```

```objc
@property (nonatomic, readonly) CIFormat workingFormat;
```

## Discussion

The working format determines the pixel format that Core Image uses to create intermediate buffers for executing filter kernels. Core Image automatically converts to and from the source and destination pixel formats of input images and output  contexts. You specify a working pixel format using the [`workingFormat`](../cicontextoption/workingformat.md) key in the `options` dictionary when creating a Core Image context.

## See Also

### Managing Resources
- [func clearCaches()](./clearcaches%28%29.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](./reclaimresources%28%29.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](./offlinegpucount%28%29.md)
  Returns the number of GPUs not currently driving a display.
- [var workingColorSpace: CGColorSpace?](./workingcolorspace.md)
  The working color space of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/workingformat)*
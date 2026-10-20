# kernelCompileTime

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var kernelCompileTime: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval kernelCompileTime;
```

## See Also

### Instance Properties
- [var kernelExecutionTime: TimeInterval](./kernelexecutiontime.md)
  The amount of time a render spent executing kernels.
- [var passCount: Int](./passcount.md)
  The number of passes the render took.
- [var pixelsProcessed: Int](./pixelsprocessed.md)
  The number of pixels the render produced executing kernels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderinfo/kernelcompiletime)*
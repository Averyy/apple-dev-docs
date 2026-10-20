# kernelExecutionTime

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The amount of time a render spent executing kernels.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var kernelExecutionTime: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval kernelExecutionTime;
```

## See Also

### Instance Properties
- [var passCount: Int](./passcount.md)
  The number of passes the render took.
- [var pixelsProcessed: Int](./pixelsprocessed.md)
  The number of pixels the render produced executing kernels.
- [var kernelCompileTime: TimeInterval](./kernelcompiletime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderinfo/kernelexecutiontime)*
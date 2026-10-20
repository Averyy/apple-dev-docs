# kernelHeight

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The height of the filter window. Must be an odd number.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var kernelHeight: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger kernelHeight;
```

## See Also

### Properties
- [var kernelWidth: Int](./kernelwidth.md)
  The width of the filter window. Must be an odd number.
- [var bias: Float](./bias.md)
  The value added to a convolved pixel before it is converted back to its intended storage format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconvolution/kernelheight)*
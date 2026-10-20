# arrayView(withDimensionCount:dimensionSizes:strides:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func arrayView(withDimensionCount numberOfDimensions: Int, dimensionSizes: UnsafePointer<Int>, strides dimStrides: UnsafePointer<Int>) -> MPSNDArray?
```

```objc
- (MPSNDArray *) arrayViewWithDimensionCount:(NSUInteger) numberOfDimensions dimensionSizes:(const NSUInteger *) dimensionSizes strides:(const NSUInteger *) dimStrides;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray/arrayview(withdimensioncount:dimensionsizes:strides:))*
# init(dataType:dimensionCount:dimensionSizes:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(dataType: MPSDataType, dimensionCount numberOfDimensions: Int, dimensionSizes: UnsafeMutablePointer<Int>)
```

```objc
+ (instancetype) descriptorWithDataType:(MPSDataType) dataType dimensionCount:(NSUInteger) numberOfDimensions dimensionSizes:(NSUInteger *) dimensionSizes;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraydescriptor/init(datatype:dimensioncount:dimensionsizes:))*
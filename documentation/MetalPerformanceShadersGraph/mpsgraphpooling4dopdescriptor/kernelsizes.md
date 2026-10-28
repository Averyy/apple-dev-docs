# kernelSizes

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

Defines the pooling window size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var kernelSizes: [NSNumber] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSArray<NSNumber *> * kernelSizes;
```

## Discussion

Must be four numbers, one for each spatial dimension, fastest running index last.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor/kernelsizes)*
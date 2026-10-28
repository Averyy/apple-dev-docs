# training

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

A parameter that enables the GRU layer to support training.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var training: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL training;
```

## Discussion

If set to `YES` then the layer will produce training state tensor as a secondary output. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphgrudescriptor/training)*
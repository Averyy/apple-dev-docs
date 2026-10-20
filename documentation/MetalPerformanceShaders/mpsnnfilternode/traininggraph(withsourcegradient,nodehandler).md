# trainingGraph(withSourceGradient:nodeHandler:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func trainingGraph(withSourceGradient gradientImage: MPSNNImageNode?, nodeHandler: MPSGradientNodeBlock? = nil) -> [MPSNNFilterNode]?
```

```objc
- (NSArray<MPSNNFilterNode *> *) trainingGraphWithSourceGradient:(MPSNNImageNode *) gradientImage nodeHandler:(MPSGradientNodeBlock) nodeHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnfilternode/traininggraph(withsourcegradient:nodehandler:))*
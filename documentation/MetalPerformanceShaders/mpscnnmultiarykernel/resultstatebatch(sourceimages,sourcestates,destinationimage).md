# resultStateBatch(sourceImages:sourceStates:destinationImage:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func resultStateBatch(sourceImages: [[MPSImage]], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSState]?
```

```objc
- (MPSStateBatch *) resultStateBatchForSourceImages:(NSArray<NSArray<MPSImage *> *> *) sourceImages sourceStates:(NSArray<NSArray<MPSState *> *> *) sourceStates destinationImage:(MPSImageBatch *) destinationImage;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel/resultstatebatch(sourceimages:sourcestates:destinationimage:))*
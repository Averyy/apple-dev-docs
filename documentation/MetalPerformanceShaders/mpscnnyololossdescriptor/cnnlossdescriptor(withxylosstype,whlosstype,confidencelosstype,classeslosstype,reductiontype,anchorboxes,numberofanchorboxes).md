# cnnLossDescriptor(withXYLossType:whLossType:confidenceLossType:classesLossType:reductionType:anchorBoxes:numberOfAnchorBoxes:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class func cnnLossDescriptor(withXYLossType XYLossType: MPSCNNLossType, whLossType WHLossType: MPSCNNLossType, confidenceLossType: MPSCNNLossType, classesLossType: MPSCNNLossType, reductionType: MPSCNNReductionType, anchorBoxes: Data, numberOfAnchorBoxes: Int) -> MPSCNNYOLOLossDescriptor
```

```objc
+ (MPSCNNYOLOLossDescriptor *) cnnLossDescriptorWithXYLossType:(MPSCNNLossType) XYLossType WHLossType:(MPSCNNLossType) WHLossType confidenceLossType:(MPSCNNLossType) confidenceLossType classesLossType:(MPSCNNLossType) classesLossType reductionType:(MPSCNNReductionType) reductionType anchorBoxes:(NSData *) anchorBoxes numberOfAnchorBoxes:(NSUInteger) numberOfAnchorBoxes;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnyololossdescriptor/cnnlossdescriptor(withxylosstype:whlosstype:confidencelosstype:classeslosstype:reductiontype:anchorboxes:numberofanchorboxes:))*
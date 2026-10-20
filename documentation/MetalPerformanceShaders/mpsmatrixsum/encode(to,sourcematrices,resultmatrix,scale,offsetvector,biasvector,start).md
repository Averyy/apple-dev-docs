# encode(to:sourceMatrices:resultMatrix:scale:offsetVector:biasVector:start:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to buffer: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], resultMatrix: MPSMatrix, scale scaleVector: MPSVector?, offsetVector: MPSVector?, biasVector: MPSVector?, start startIndex: Int)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) buffer sourceMatrices:(NSArray<MPSMatrix *> *) sourceMatrices resultMatrix:(MPSMatrix *) resultMatrix scaleVector:(MPSVector *) scaleVector offsetVector:(MPSVector *) offsetVector biasVector:(MPSVector *) biasVector startIndex:(NSUInteger) startIndex;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsum/encode(to:sourcematrices:resultmatrix:scale:offsetvector:biasvector:start:))*
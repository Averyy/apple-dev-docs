# encode(commandBuffer:sourceImages:destinationState:destinationStateIsTemporary:)

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
func encode(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationState outState: AutoreleasingUnsafeMutablePointer<MPSState?>, destinationStateIsTemporary isTemporary: Bool) -> MPSImage
```

```objc
- (MPSImage *) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImages:(NSArray<MPSImage *> *) sourceImages destinationState:(MPSState **) outState destinationStateIsTemporary:(BOOL) isTemporary;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel/encode(commandbuffer:sourceimages:destinationstate:destinationstateistemporary:))*
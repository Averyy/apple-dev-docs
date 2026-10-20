# MPSGetCustomKernelBatchedSourceIndex(_:_:_:)

**Framework**: Metal Performance Shaders  
**Kind**: func  
**Role**: Function

Returns the index of the specified batched source texture argument.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MPSGetCustomKernelBatchedSourceIndex(_ c: MPSCustomKernelArgumentCount, _ sourceIndex: UInt, _ MPSMaxTextures: UInt) -> UInt
```

```c
static unsigned long MPSGetCustomKernelBatchedSourceIndex(MPSCustomKernelArgumentCount c, unsigned long sourceIndex, unsigned long MPSMaxTextures);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsgetcustomkernelbatchedsourceindex(_:_:_:))*
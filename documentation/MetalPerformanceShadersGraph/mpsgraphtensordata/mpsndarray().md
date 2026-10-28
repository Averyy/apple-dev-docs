# mpsndarray()

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Return an mpsndarray object will copy contents if the contents are not stored in an MPS ndarray.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func mpsndarray() -> MPSNDArray
```

```objc
- (MPSNDArray *) mpsndarray;
```

## Return Value

A valid MPSNDArray, or nil if allocation fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/mpsndarray())*
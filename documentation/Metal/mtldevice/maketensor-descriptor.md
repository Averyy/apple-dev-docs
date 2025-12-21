# makeTensor(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a tensor by allocating new memory.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeTensor(descriptor: MTLTensorDescriptor) throws -> any MTLTensor
```

#### Return Value

A new tensor instance that Metal configures using `descriptor` or `nil` if an error occurred.

## Parameters

- `descriptor`: A description of the properties for the new tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maketensor(descriptor:))*
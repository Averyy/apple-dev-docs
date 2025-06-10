# makeTensor(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a tensor by allocating new memory.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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
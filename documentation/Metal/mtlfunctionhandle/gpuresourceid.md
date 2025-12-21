# gpuResourceID

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var gpuResourceID: MTLResourceID { get }
```

#### Discussion

Handle of the GPU resource suitable for storing in an Intersection Function Buffer.

The handle must have been created from an intersection function annotated with the `intersection_function_buffer` tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionhandle/gpuresourceid)*
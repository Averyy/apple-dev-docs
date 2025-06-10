# gpuResourceID

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var gpuResourceID: MTLResourceID { get }
```

#### Discussion

The handle must have been created from an intersection function annotated with the `intersection_function_buffer` tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionhandle/gpuresourceid)*
# buffer

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The buffer that provides the underlying storage for this plane, or `nil` if no buffer was provided at initialization.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var buffer: (any MTLBuffer)? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplane/buffer)*
# buffer

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A buffer instance this tensor shares its storage with or nil if this tensor does not wrap an underlying buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var buffer: (any MTLBuffer)? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/buffer)*
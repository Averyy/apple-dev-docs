# isContiguous

**Framework**: Core Media  
**Kind**: property

Determine whether the block buffer is contiguous.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var isContiguous: Bool { get }
```

#### Discussion

`true` if block buffer references a single contiguous memory block `false` otherwise. Also `false` if the buffer is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/iscontiguous)*
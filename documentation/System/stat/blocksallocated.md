# blocksAllocated

**Framework**: System  
**Kind**: property

Number of 512-byte blocks allocated

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var blocksAllocated: Int64 { get set }
```

#### Discussion

The semantics of this property are tied to the underlying C `st_blocks` field, which can have file-system–dependent behavior.

The corresponding C property is `st_blocks`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/blocksallocated)*
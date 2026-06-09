# sizeAllocated

**Framework**: System  
**Kind**: property

Total size allocated, in bytes

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
var sizeAllocated: Int64 { get }
```

#### Discussion

The semantics of this property are tied to the underlying C `st_blocks` field, which can have file-system–dependent behavior.

> **Note**: Calculated as `512 * blocksAllocated`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/sizeallocated)*
# sizeAllocated

**Framework**: System  
**Kind**: property

Total size allocated, in bytes

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var sizeAllocated: Int64 { get }
```

#### Discussion

The semantics of this property are tied to the underlying C `st_blocks` field, which can have file-system–dependent behavior.

> **Note**: Calculated as `512 * blocksAllocated`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/sizeallocated)*
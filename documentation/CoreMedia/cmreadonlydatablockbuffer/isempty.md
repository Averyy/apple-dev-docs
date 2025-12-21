# isEmpty

**Framework**: Core Media  
**Kind**: property

Indicates whether the block buffer is empty.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Discussion

Indicates whether the block buffer is empty, i.e., devoid of any memory blocks or block buffer references. Note that a block buffer containing a not-yet allocated memory block is not considered empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/isempty)*
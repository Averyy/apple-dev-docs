# isEmpty

**Framework**: Core Media  
**Kind**: property

Indicates whether the block buffer is empty.

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
var isEmpty: Bool { get }
```

#### Discussion

Indicates whether the block buffer is empty, i.e., devoid of any memory blocks or block buffer references. Note that a block buffer containing a not-yet allocated memory block is not considered empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/isempty)*
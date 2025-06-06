# didModifyRange(_:)

**Framework**: Metal  
**Kind**: method

Informs the GPU that the CPU has modified a section of the buffer.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.11+

## Declaration

```swift
func didModifyRange(_ range: Range<Int>)
```

#### Discussion

If you write information to a buffer created with the [`MTLStorageMode.managed`](mtlstoragemode/managed.md) storage mode, you must call this method to inform the GPU that the information has changed. If you execute GPU commands that read the data without calling this method first, the behavior is undefined.

## Parameters

- `range`: The range of bytes that have been modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/didmodifyrange(_:))*
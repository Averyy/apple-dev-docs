# didModifyRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Informs the GPU that the CPU has modified a section of the buffer.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0

## Declaration

```objc
- (void) didModifyRange:(NSRange) range;
```

## Mentions

- [Synchronizing a managed resource in macOS](../synchronizing-a-managed-resource-in-macos.md)

## Discussion

If you write information to a buffer created with the [`MTLStorageMode.managed`](../mtlstoragemode/managed.md) storage mode, you need to call this method to inform the GPU that the information has changed. If you execute GPU commands that read from the modified sections without calling this method first, the behavior is undefined.

## Parameters

- `range`: The range of bytes that were modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/didmodifyrange:)*
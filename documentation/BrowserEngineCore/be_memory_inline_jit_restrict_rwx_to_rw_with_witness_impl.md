# be_memory_inline_jit_restrict_rwx_to_rw_with_witness_impl

**Framework**: BrowserEngineCore  
**Kind**: func  
**Role**: Function

Makes a region of memory writable for use in just-in-time (JIT) compilation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+
- visionOS 1.1+

## Declaration

```c
extern void be_memory_inline_jit_restrict_rwx_to_rw_with_witness_impl();
```

## Overview

You don’t call this function directly. Call [`be_memory_inline_jit_restrict_rwx_to_rw_with_witness`](./be_memory_inline_jit_restrict_rwx_to_rw_with_witness.md) instead.

## See Also

### Memory-protection implementation
- [be_memory_inline_jit_restrict_rwx_to_rx_with_witness_impl](./be_memory_inline_jit_restrict_rwx_to_rx_with_witness_impl.md)
  Makes a region of memory executable for use in just-in-time (JIT) compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/be_memory_inline_jit_restrict_rwx_to_rw_with_witness_impl)*
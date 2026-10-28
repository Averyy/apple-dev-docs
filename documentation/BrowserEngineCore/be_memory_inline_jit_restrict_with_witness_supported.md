# be_memory_inline_jit_restrict_with_witness_supported

**Framework**: BrowserEngineCore  
**Kind**: func  
**Role**: Function

Reports whether write protection for just-in-time (JIT) compilation is available.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+
- visionOS 1.1+

## Declaration

```c
extern int be_memory_inline_jit_restrict_with_witness_supported();
```

## Return Value

`true` if the memory-protection functions are available; `false` otherwise.

## Overview

If this function returns `true`, your browser’s web content extension can use [`be_memory_inline_jit_restrict_rwx_to_rw_with_witness`](./be_memory_inline_jit_restrict_rwx_to_rw_with_witness.md) and [`be_memory_inline_jit_restrict_rwx_to_rx_with_witness`](./be_memory_inline_jit_restrict_rwx_to_rx_with_witness.md) to protect memory that you use to compile and run JIT code. Otherwise, these functions aren’t available.

For more information, see [Protecting code compiled just in time](../BrowserEngineKit/protecting-code-compiled-just-in-time.md).

## See Also

### JIT compilation
- [be_memory_inline_jit_restrict_rwx_to_rw_with_witness](./be_memory_inline_jit_restrict_rwx_to_rw_with_witness.md)
  Makes a region of memory writable for use in just-in-time (JIT) compilation.
- [be_memory_inline_jit_restrict_rwx_to_rx_with_witness](./be_memory_inline_jit_restrict_rwx_to_rx_with_witness.md)
  Makes a region of memory executable for use in just-in-time (JIT) compilation.
- [var BE_JIT_WRITE_PROTECT_TAG: Int](./be_jit_write_protect_tag.md)
  A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/be_memory_inline_jit_restrict_with_witness_supported)*
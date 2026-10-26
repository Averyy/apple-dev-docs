# BE_JIT_WRITE_PROTECT_TAG

**Framework**: BrowserEngineCore  
**Kind**: var  
**Role**: Global Variable

A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- visionOS

## Declaration

```swift
var BE_JIT_WRITE_PROTECT_TAG: Int { get }
```

```c
#define BE_JIT_WRITE_PROTECT_TAG
```

## See Also

### JIT compilation
- [be_memory_inline_jit_restrict_with_witness_supported](./be_memory_inline_jit_restrict_with_witness_supported.md)
  Reports whether write protection for just-in-time (JIT) compilation is available.
- [be_memory_inline_jit_restrict_rwx_to_rw_with_witness](./be_memory_inline_jit_restrict_rwx_to_rw_with_witness.md)
  Makes a region of memory writable for use in just-in-time (JIT) compilation.
- [be_memory_inline_jit_restrict_rwx_to_rx_with_witness](./be_memory_inline_jit_restrict_rwx_to_rx_with_witness.md)
  Makes a region of memory executable for use in just-in-time (JIT) compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginecore/be_jit_write_protect_tag)*
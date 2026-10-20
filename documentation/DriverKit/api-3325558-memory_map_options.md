# Memory Map Options

**Framework**: DriverKit  
**Role**: API Collection

Options that describe how to configure a memory-mapped buffer.

## Topics

### Options
- [kIOMemoryMapFixedAddress](./kiomemorymapfixedaddress.md)
  The memory maps to a specific address.
- [kIOMemoryMapReadOnly](./kiomemorymapreadonly.md)
  The memory maps as read-only.
- [kIOMemoryMapCacheModeDefault](./kiomemorymapcachemodedefault.md)
  The memory maps using the default cache mode.
- [kIOMemoryMapCacheModeInhibit](./kiomemorymapcachemodeinhibit.md)
  The memory maps using the inhibited cache mode.
- [kIOMemoryMapCacheModeCopyback](./kiomemorymapcachemodecopyback.md)
  The memory maps using the copy-back cache mode.
- [kIOMemoryMapCacheModeWriteThrough](./kiomemorymapcachemodewritethrough.md)
  The memory maps using the write-through cache mode.

## See Also

### Mapping to the Caller’s Address Space
- [CreateMapping](./iomemorydescriptor/createmapping.md)
  Maps the contents of the memory block to the address space of the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/3325558-memory_map_options)*
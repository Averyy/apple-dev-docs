# mach_msg_ool_descriptor_t

**Framework**: DriverKit  
**Kind**: struct

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef struct { ... } mach_msg_ool_descriptor_t;
```

## Topics

### Getting the Properties
- [address](mach_msg_ool_descriptor_t/address.md)
- [copy](mach_msg_ool_descriptor_t/copy.md)
- [deallocate](mach_msg_ool_descriptor_t/deallocate.md)
- [pad1](mach_msg_ool_descriptor_t/pad1.md)
- [size](mach_msg_ool_descriptor_t/size.md)
- [type](mach_msg_ool_descriptor_t/type.md)

## See Also

- [mach_msg_bits_t](mach_msg_bits_t.md)
- [mach_msg_copy_options_t](mach_msg_copy_options_t.md)
- [mach_msg_descriptor_type_t](mach_msg_descriptor_type_t.md)
- [mach_msg_id_t](mach_msg_id_t.md)
- [mach_msg_size_t](mach_msg_size_t.md)
- [mach_msg_type_name_t](mach_msg_type_name_t.md)
- [mach_msg_body_t](mach_msg_body_t.md)
- [mach_msg_header_t](mach_msg_header_t.md)
- [mach_msg_max_trailer_t](mach_msg_max_trailer_t.md)
- [mach_msg_port_descriptor_t](mach_msg_port_descriptor_t.md)
- [mach_timebase_info_data_t](mach_timebase_info_data_t.md)
  Raw Mach Time API In general prefer to use the <time.h> API clock_gettime_nsec_np(3), which deals in the same clocks (and more) in ns units. Conversion of ns to (resp. from) tick units as returned by the mach time APIs is performed by division (resp. multiplication) with the fraction returned by mach_timebase_info().


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/mach_msg_ool_descriptor_t)*
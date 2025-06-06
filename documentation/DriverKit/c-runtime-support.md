# C++ Runtime Support

**Framework**: DriverKit

Examine low-level types that DriverKit uses to support kernel-level operations.

## Topics

### Object Support
- [OSObjectAllocate](osobjectallocate.md)
  Helper function for OSTypeAlloc(). Not to be called directly.
- [OSObjectRetain](osobjectretain.md)
- [OSObjectRelease](osobjectrelease.md)
### Additional Types
- [IOReturn](ioreturn.md)
- [IOOptionBits](iooptionbits.md)
- [integer_t](integer_t.md)
- [natural_t](natural_t.md)
- [kern_return_t](kern_return_t.md)
- [IOItemCount](ioitemcount.md)
- [IOVersion](ioversion.md)
### Log Support
- [OSObjectLog](osobjectlog.md)
- [IOLogBuffer](iologbuffer.md)
- [crc32](crc32.md)
### Base Classes
- [OSMetaClass](osmetaclass.md)
  Base class for DriverKit runtime class system. Not called directly.
- [OSMetaClassBase](osmetaclassbase.md)
  Base class for DriverKit objects.
### RPC Support
- [IORPC](iorpc.md)
- [IORPCMessage](iorpcmessage.md)
- [IORPCMessageMach](iorpcmessagemach.md)
- [IORPCMessageErrorReturn](iorpcmessageerrorreturn.md)
- [OSClassLoadInformation](osclassloadinformation.md)
- [OSClassDescription](osclassdescription.md)
- [OSDispatchMethod](osdispatchmethod.md)
- [RPC Message ID](3222959-rpc_message_id.md)
- [RPC Message Types](3222960-rpc_message_types.md)
- [RPC Capabilities](3222961-rpc_capabilities.md)
- [RPC Version](3353062-rpc_version.md)
- [IORPCMessageFromMach](iorpcmessagefrommach.md)
### Mach Ports
- [mach_port_name_t](mach_port_name_t.md)
- [mach_port_t](mach_port_t.md)
### Mach Timebase
- [mach_absolute_time](mach_absolute_time.md)
  Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), this clock does not increment while the system is asleep.
- [mach_continuous_time](mach_continuous_time.md)
  Returns current value of a clock that increments monotonically in tick units (starting at an arbitrary point), including while the system is asleep.
- [mach_timebase_info](mach_timebase_info-c.func.md)
  Returns fraction to multiply a value in mach tick units with to convert it to nanoseconds.
- [mach_timebase_info_t](mach_timebase_info_t.md)
- [Time Scales](3223112-time_scales.md)
### Mach Messages
- [mach_msg_bits_t](mach_msg_bits_t.md)
- [mach_msg_copy_options_t](mach_msg_copy_options_t.md)
- [mach_msg_descriptor_type_t](mach_msg_descriptor_type_t.md)
- [mach_msg_id_t](mach_msg_id_t.md)
- [mach_msg_size_t](mach_msg_size_t.md)
- [mach_msg_type_name_t](mach_msg_type_name_t.md)
- [mach_msg_body_t](mach_msg_body_t.md)
- [mach_msg_header_t](mach_msg_header_t.md)
- [mach_msg_max_trailer_t](mach_msg_max_trailer_t.md)
- [mach_msg_ool_descriptor_t](mach_msg_ool_descriptor_t.md)
- [mach_msg_port_descriptor_t](mach_msg_port_descriptor_t.md)
- [mach_timebase_info_data_t](mach_timebase_info_data_t.md)
  Raw Mach Time API In general prefer to use the <time.h> API clock_gettime_nsec_np(3), which deals in the same clocks (and more) in ns units. Conversion of ns to (resp. from) tick units as returned by the mach time APIs is performed by division (resp. multiplication) with the fraction returned by mach_timebase_info().
### Boot Support
- [IOParseBootArgNumber](ioparsebootargnumber.md)
  Parses any boot arguments in the macOS kernel boot-args.
- [IOParseBootArgString](ioparsebootargstring.md)
  Parses any boot arguments in the macOS kernel boot-args.
### Thread Utilities
- [IODelay](iodelay.md)
  Sleep the calling thread for a number of microseconds.
- [IOSleep](iosleep.md)
  Sleep the calling thread for a number of milliseconds.
### Additional Utilities
- [OSReportWithBacktrace](osreportwithbacktrace.md)
  Generates a backtrace and message for debugging.
- [OSSynchronizeIO](ossynchronizeio.md)
  Performs an `mfence` instruction on Intel-based Mac computers.

## See Also

- [OSDynamicCast](osdynamiccast.md)
  Casts an object safely to the specified type, if possible.
- [OSRequiredCast](osrequiredcast.md)
  Casts the object to the specified type, stopping the process if the object isn’t of the correct type.
- [IMPL](impl.md)
  Tells the system that the superclass implementation of this method runs in the kernel.
- [TYPE](type.md)
  Annotates a method declaration to indicate that it conforms to an existing method signature.
- [QUEUENAME](queuename.md)
  Tells the system to execute a method on the dispatch queue with the specified name.
- [SUPERDISPATCH](superdispatch.md)
  Tells the system to execute the superclass’ implementation of the current method in the kernel.
- [IIG_KERNEL](iig_kernel.md)
  Tells the system that the class or method runs inside the kernel.
- [LOCAL](local.md)
  Tells the system that the method runs locally in the driver extension’s process space.
- [LOCALONLY](localonly.md)
  Tells the system that the class or method runs locally in the driver extension’s process space.
- [Error Codes](error-codes.md)
  Determine the reason an operation fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/c-runtime-support)*
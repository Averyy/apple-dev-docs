# SUPERDISPATCH

**Framework**: DriverKit  
**Kind**: macro

Tells the system to execute the superclass’ implementation of the current method in the kernel.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define SUPERDISPATCH
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Discussion

When calling the DriverKit implementation of a method that runs in the kernel, use this macro to bridge from your driver extension’s process space to the superclass’ version of the method. You must use this macro to call inherited DriverKit methods annotated with the [`IIG_KERNEL`](iig_kernel.md) macro.

To use this macro, call the original method without the `super` prefix and insert this macro as the final parameter in the parameter list. For example, the following code shows how to call the inherited version of the [`Start`](ioservice/start.md) method from a custom [`IOService`](ioservice.md) subclass.

```objc
kern_return_t IMPL(MyCustomService, Start)
{
   kern_return_t ret;
   ret = Start(provider, SUPERDISPATCH);

   // Other Start code...
}
```

Don’t use this macro when calling the inherited version of a DriverKit method marked with the [`LOCALONLY`](localonly.md) macro.

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
- [IIG_KERNEL](iig_kernel.md)
  Tells the system that the class or method runs inside the kernel.
- [LOCAL](local.md)
  Tells the system that the method runs locally in the driver extension’s process space.
- [LOCALONLY](localonly.md)
  Tells the system that the class or method runs locally in the driver extension’s process space.
- [Error Codes](error-codes.md)
  Determine the reason an operation fails.
- [C++ Runtime Support](c-runtime-support.md)
  Examine low-level types that DriverKit uses to support kernel-level operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/superdispatch)*
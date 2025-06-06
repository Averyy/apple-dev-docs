# IMPL

**Framework**: DriverKit  
**Kind**: macro

Tells the system that the superclass implementation of this method runs in the kernel.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define IMPL(classname, name)
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Discussion

Use this macro when overriding any methods that are adorned directly (or indirectly via their class) with the [`IIG_KERNEL`](iig_kernel.md) macro. For example, use it to define the implementation of custom [`Start`](ioservice/start.md) and [`Stop`](ioservice/stop.md) methods in an [`IOService`](ioservice.md) subclass. The macro tells the compiler to add binding code between the method running locally in your driver extension’s process space and the superclass method running in the kernel. Don’t add this macro when overriding methods declared with the [`LOCAL`](local.md) or [`LOCALONLY`](localonly.md) macros.

When using the [`IMPL`](impl.md) macro to define your method, don’t include the method parameters as part of your definition. The compiler automatically inserts the appropriate parameters using information from the superclass’ definition. For example, the following code shows how to declare a custom implementation of the [`Start`](ioservice/start.md) method:

```objc
kern_return_t IMPL(MyCustomService, Start) 
{
   // Custom code here...
}
```

## Parameters

- `classname`: The name of your custom class.
- `name`: The name of the DriverKit method you are overriding in your custom subclass.

## See Also

- [OSDynamicCast](osdynamiccast.md)
  Casts an object safely to the specified type, if possible.
- [OSRequiredCast](osrequiredcast.md)
  Casts the object to the specified type, stopping the process if the object isn’t of the correct type.
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
- [C++ Runtime Support](c-runtime-support.md)
  Examine low-level types that DriverKit uses to support kernel-level operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/impl)*
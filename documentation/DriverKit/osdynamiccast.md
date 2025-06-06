# OSDynamicCast

**Framework**: DriverKit  
**Kind**: macro

Casts an object safely to the specified type, if possible.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define OSDynamicCast(type, inst)
```

#### Return Value

The object cast to the specified type, or `NULL` if the cast could not be performed safely.

#### Discussion

Use this macro instead of the standard C++ RTTI type-casting operator to cast objects to specific types. The following example shows how to cast some object to the [`OSString`](osstring.md) class. If the object cannot be cast to a string, the macro sets the `string` variable to `NULL`.

```objc
OSString string = OSDynamicCast(OSString, anObject)
```

## Parameters

- `type`: The name of the desired class type as a raw token, not as a string or macro.
- `inst`: The object to cast to the specified type.

## See Also

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
- [C++ Runtime Support](c-runtime-support.md)
  Examine low-level types that DriverKit uses to support kernel-level operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdynamiccast)*
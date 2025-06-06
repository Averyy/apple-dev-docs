# OSRequiredCast

**Framework**: DriverKit  
**Kind**: macro

Casts the object to the specified type, stopping the process if the object isn’t of the correct type.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define OSRequiredCast(type, inst)
```

#### Return Value

The object cast to the specified type.

#### Discussion

Use this macro when you require the object to be the specified type, and you are sure that it’s the specified type. The following example shows how to cast some object to the [`OSString`](osstring.md) class. If the object cannot be cast to a string, the macro terminates the process.

```objc
OSString string = OSDynamicCast(OSString, anObject)
```

## Parameters

- `type`: The name of the desired class type as a raw token, not as a string or macro.
- `inst`: The object to cast to the specified type.

## See Also

- [OSDynamicCast](osdynamiccast.md)
  Casts an object safely to the specified type, if possible.
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osrequiredcast)*
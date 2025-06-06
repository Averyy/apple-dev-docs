# TYPE

**Framework**: DriverKit  
**Kind**: macro

Annotates a method declaration to indicate that it conforms to an existing method signature.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
#define TYPE(p)
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Discussion

Typically, you use this macro to implement DriverKit callbacks using your own custom methods. The macro lets you ignore the original method’s name and choose any name you want. Your method must still declare the same parameters and return type as the original method. For example, the following code shows how to declare a custom version of the [`DataAvailable`](iodataqueuedispatchsource/dataavailable.md) method of [`IODataQueueDispatchSource`](iodataqueuedispatchsource.md) in your header file.

```swift
virtual void MyCustomDataAvailable (OSAction *action) TYPE(IODataQueueDispatchSource::DataAvailable);
```

This macro generates the following convenient symbols that you can use when configuring actions involving your custom method:

- A message ID constant you can pass to the [`Create`](https://developer.apple.com/documentation/kernel/osaction/3438206-create) method of [`OSAction`](osaction.md). The constant takes the form `<ClassName>_<MethodName>_ID`. For example, if you add the [`TYPE`](type.md) macro to the `ReceiveData` method of your custom `MyDriver` class, the corresponding message ID constant is `MyDriver_ReceiveData_ID`.
- A `CreateAction_<Method>` function that creates an [`OSAction`](osaction.md) object targeting your custom method. For example, if the name of your custom method is `HandleTimer`, the name of the generated function is `CreateActionHandleTimer`.

## Parameters

- `p`: The class and method name to which the method conforms. Specify this value using the format  . Specify the class and method names directly, and do not use a string.

## See Also

- [OSDynamicCast](osdynamiccast.md)
  Casts an object safely to the specified type, if possible.
- [OSRequiredCast](osrequiredcast.md)
  Casts the object to the specified type, stopping the process if the object isn’t of the correct type.
- [IMPL](impl.md)
  Tells the system that the superclass implementation of this method runs in the kernel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/type)*
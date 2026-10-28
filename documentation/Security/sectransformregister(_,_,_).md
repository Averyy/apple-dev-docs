# SecTransformRegister(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Registers a custom transform.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecTransformRegister(_ uniqueName: CFString, _ createTransformFunction: SecTransformCreateFP, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

```c
extern Boolean SecTransformRegister(CFStringRef uniqueName, SecTransformCreateFP createTransformFunction, CFErrorRef*error);
```

## Return Value

A Boolean that is set to [`true`](../Swift/true.md) if the custom transform was registered and [`false`](../Swift/false.md) otherwise

## Parameters

- `uniqueName`: A unique name for this custom transform. It is recommended that a reverse DNS name be used for the name of your custom transform
- `createTransformFunction`: A [`SecTransformCreateFP`](./sectransformcreatefp.md) function pointer. The function must return a [`SecTransformInstanceBlock`](./sectransforminstanceblock.md) block. Call block_copy on this block before returning it. Failure to do so results in undefined behavior.
- `error`: A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass `NULL` to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformregister(_:_:_:))*
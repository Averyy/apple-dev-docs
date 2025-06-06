# SecTransformRegister(_:_:_:)

**Framework**: Security  
**Kind**: func

Registers a custom transform.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformRegister(_ uniqueName: CFString, _ createTransformFunction: SecTransformCreateFP, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

#### Return Value

A Boolean that is set to [`true`](https://developer.apple.com/documentation/swift/true) if the custom transform was registered and [`false`](https://developer.apple.com/documentation/swift/false) otherwise

## Parameters

- `uniqueName`: A unique name for this custom transform. It is recommended that a reverse DNS name be used for the name of your custom transform
- `createTransformFunction`: A   function pointer. The function must return a   block. Call block_copy on this block before returning it. Failure to do so results in undefined behavior.
- `error`: A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass   to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformregister(_:_:_:))*
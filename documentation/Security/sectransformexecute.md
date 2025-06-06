# SecTransformExecute(_:_:)

**Framework**: Security  
**Kind**: func

Executes a transform or transform group synchronously.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformExecute(_ transformRef: SecTransform, _ errorRef: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFTypeRef
```

#### Return Value

This is the result of the transform. The specific value is determined by the transform being executed.

#### Discussion

There are two phases that occur when executing a transform. The first phase checks to see if the transforms have all of their required attributes set. If a GroupTransform is being executed, then a required attribute for a transform is valid if it is connected to another attribute that supplies the required value. If any of the required attributes are not set or connected then SecTransformExecute will not run the transform but will return NULL and the apporiate error is placed in the error parameter if it is not NULL.

The second phase is the actual execution of the transform. SecTransformExecute executes the transform or GroupTransform and when all of the processing is completed it returns the result. If an error occurs during execution, then all processing will stop and NULL will be returned and the appropriate error will be placed in the error parameter if it is not NULL.

## Parameters

- `transformRef`: The transform to execute.
- `errorRef`: An optional pointer to a CFErrorRef. This value will be set if an error occurred during initialization or execution of the transform or group. If not NULL the caller will be responsible for releasing the returned CFErrorRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformexecute(_:_:))*
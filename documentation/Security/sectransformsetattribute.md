# SecTransformSetAttribute(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Sets a static value for an attribute in a transform.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformSetAttribute(_ transformRef: SecTransform, _ key: CFString, _ value: CFTypeRef, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

#### Return Value

A Boolean set to [`true`](https://developer.apple.com/documentation/swift/true) if the call succeeds. Otherwise, the `error` parameter contains information about the failure.

#### Discussion

This function is useful for things like iteration counts and other non-changing values. It returns an error and the named attribute is not changed if [`SecTransformExecute(_:_:)`](sectransformexecute(_:_:).md) has already been called on the transform.

Compare this function with the [`SecTransformConnectTransforms(_:_:_:_:_:_:)`](sectransformconnecttransforms(_:_:_:_:_:_:).md) function which sets derived data.

## Parameters

- `transformRef`: The transform whose attribute is to be set.
- `key`: The name of the attribute to be set. See   for a list of valid keys and possible values.
- `value`: The static value to set for the named attribute.
- `error`: A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass   to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformsetattribute(_:_:_:_:))*
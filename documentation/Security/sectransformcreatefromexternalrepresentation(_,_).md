# SecTransformCreateFromExternalRepresentation(_:_:)

**Framework**: Security  
**Kind**: func

Creates a transform instance from a dictionary of parameters.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformCreateFromExternalRepresentation(_ dictionary: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

#### Return Value

A pointer to a SecTransformRef object. You must release the object with CFRelease when you are done with it. A NULL will be returned if an error occurred during initialization, and if the error parameter is non-null, it contains the specific error data.

## Parameters

- `dictionary`: The dictionary of parameters.
- `error`: An optional pointer to a CFErrorRef. This value is set if an error occurred. If not NULL the caller is responsible for releasing the CFErrorRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcreatefromexternalrepresentation(_:_:))*
# SecTransformCreateFP

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A pointer to a function that creates a new instance of a custom transform.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
typealias SecTransformCreateFP = (CFString, SecTransform, SecTransformImplementationRef) -> () -> Unmanaged<CFError>?
```

```c
typedef struct __CFError *(^(*)(const struct __CFString *, const void *, const struct OpaqueSecTransformImplementation *))(void) SecTransformCreateFP;
```

#### Return Value

A [`SecTransformInstanceBlock`](./sectransforminstanceblock.md) that is used to create a new instance of a custom transform.

#### Discussion

Provide a function of this type to the [`SecTransformCreate(_:_:)`](./sectransformcreate%28_,_%29.md) function when creating a custom transform. The function defined here returns an object of type [`SecTransformInstanceBlock`](./sectransforminstanceblock.md) that provides the implementation of all of the overrides necessary to create the custom transform. This returned [`SecTransformInstanceBlock`](./sectransforminstanceblock.md) is also where the “instance” variables for the custom transform may be defined.

## Parameters

- `name`: The name of the new custom transform. This name must be unique.
- `newTransform`: The newly created transform.
- `ref`: A reference that is bound to an instance of a custom transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcreatefp)*
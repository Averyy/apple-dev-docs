# SecTransformCreate(_:_:)

**Framework**: Security  
**Kind**: func

Creates a transform computation object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformCreate(_ name: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

#### Return Value

A pointer to a new transform or `NULL` on failure. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this object’s memory when you are done with it.

## Parameters

- `name`: The type of transform to create. Use one of the pre-defined transform types or a custom type that you previously registered using  .
- `error`: A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass   to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcreate(_:_:))*
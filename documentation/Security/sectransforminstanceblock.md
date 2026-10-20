# SecTransformInstanceBlock

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A block that you return from a transform creation function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SecTransformInstanceBlock = () -> Unmanaged<CFError>?
```

```c
typedef struct __CFError *(^)(void) SecTransformInstanceBlock;
```

#### Return Value

A an error object if an error occurred.

#### Discussion

You return a block of this type from the custom transform creation function of type [`SecTransformCreateFP`](./sectransformcreatefp.md) that you register with the [`SecTransformRegister(_:_:_:)`](./sectransformregister%28_,_,_%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransforminstanceblock)*
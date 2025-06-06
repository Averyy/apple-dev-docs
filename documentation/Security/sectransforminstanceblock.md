# SecTransformInstanceBlock

**Framework**: Security  
**Kind**: typealias

A block that you return from a transform creation function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SecTransformInstanceBlock = () -> Unmanaged<CFError>?
```

#### Return Value

A an error object if an error occurred.

#### Discussion

You return a block of this type from the custom transform creation function of type [`SecTransformCreateFP`](sectransformcreatefp.md) that you register with the [`SecTransformRegister(_:_:_:)`](sectransformregister(_:_:_:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransforminstanceblock)*
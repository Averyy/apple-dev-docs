# grantCapability(_:invalidationHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Grants the specified capability to the process and observes an invalidation closure.

**Availability**:
- iOS 17.6+
- iPadOS 17.6+

## Declaration

```swift
func grantCapability(_ capability: ProcessCapability, invalidationHandler: @escaping () -> Void) throws -> ProcessCapability.Grant
```

## Return Value

A [`ProcessCapability.Grant`](../processcapability/grant.md) object that represents the granted capability.

## Discussion

When the process no longer needs the capability, call [`invalidate()`](../processcapability/grant/invalidate%28%29.md) on the returned object.

## Parameters

- `capability`: The capability to grant.
- `invalidationHandler`: A closure that the system calls when the capability becomes invalid.

## See Also

### Coordinating processes
- [func grantCapability(ProcessCapability) throws -> ProcessCapability.Grant](./grantcapability%28_%29.md)
  Grants the specified capability to the process.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](./createvisibilitypropagationinteraction%28%29.md)
  Returns an interaction that associates a view with the rendering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingprocess/grantcapability(_:invalidationhandler:))*
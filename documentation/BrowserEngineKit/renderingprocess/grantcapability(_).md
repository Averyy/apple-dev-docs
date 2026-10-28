# grantCapability(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Grants the specified capability to the process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func grantCapability(_ capability: ProcessCapability) throws -> ProcessCapability.Grant
```

## Return Value

A [`ProcessCapability.Grant`](../processcapability/grant.md) object that represents the granted capability.

## Discussion

When the process no longer needs the capability, call [`invalidate()`](../processcapability/grant/invalidate%28%29.md) on the returned object.

## Parameters

- `capability`: The capability to grant.

## See Also

### Coordinating processes
- [func grantCapability(ProcessCapability, invalidationHandler: () -> Void) throws -> ProcessCapability.Grant](./grantcapability%28_,invalidationhandler%29.md)
  Grants the specified capability to the process and observes an invalidation closure.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](./createvisibilitypropagationinteraction%28%29.md)
  Returns an interaction that associates a view with the rendering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingprocess/grantcapability(_:))*
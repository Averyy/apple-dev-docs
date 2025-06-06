# grantCapability(_:invalidationHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method

Grants the specified capability to the process, calling the handler when the capability becomes invalid.

**Availability**:
- iOS 17.6+
- iPadOS 17.6+

## Declaration

```swift
func grantCapability(_ capability: ProcessCapability, invalidationHandler: @escaping () -> Void) throws -> ProcessCapability.Grant
```

#### Return Value

A [`ProcessCapability.Grant`](processcapability/grant.md) object that represents the granted capability.

#### Overview

When the process no longer needs the capability, call [`invalidate()`](processcapability/grant/invalidate().md) on the returned object.

## Parameters

- `capability`: The capability to grant.
- `invalidationHandler`: A closure that the system calls when the capability becomes invalid.

## See Also

- [func grantCapability(ProcessCapability) throws -> ProcessCapability.Grant](renderingprocess/grantcapability(_:).md)
  Grants the specified capability to the process.
- [func createVisibilityPropagationInteraction() -> any UIInteraction](renderingprocess/createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the rendering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingprocess/grantcapability(_:invalidationhandler:))*
# grantCapability:error:invalidationHandler:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Grants the specified capability to the process, invoking the handler when the capability becomes invalid.

**Availability**:
- iOS 17.6+
- iPadOS 17.6+

## Declaration

```objc
- (id<BEProcessCapabilityGrant>) grantCapability:(BEProcessCapability *) capability error:(NSError **) error invalidationHandler:(void (^)()) invalidationHandler;
```

## Return Value

A [`BEProcessCapabilityGrant`](../beprocesscapabilitygrant.md) object that represents the granted capability, or `nil` if an error occurs.

## Discussion

When the process no longer needs the capability, call [`invalidate`](../beprocesscapabilitygrant/invalidate.md) on the returned object.

## Parameters

- `capability`: The capability to grant.
- `error`: If an error occurs, upon return contains an [`NSError`](../../Foundation/nserror.md) object that describes the problem. If you don’t want information about errors that happen, pass in `NULL`.
- `invalidationHandler`: A block the system calls when the capability becomes invalid.

## See Also

### Coordinating processes
- [- grantCapability:error:](./grantcapability_error_.md)
  Grants the specified capability to the process.
- [- createVisibilityPropagationInteraction](./createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the rendering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berenderingprocess/grantcapability:error:invalidationhandler:)*
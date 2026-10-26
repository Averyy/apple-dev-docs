# grantCapability:error:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Grants the specified capability to the process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
- (id<BEProcessCapabilityGrant>) grantCapability:(BEProcessCapability *) capability error:(NSError **) error;
```

#### Return Value

A [`BEProcessCapabilityGrant`](../beprocesscapabilitygrant.md) object that represents the granted capability, or `nil` if an error occurs.

#### Discussion

When the process no longer needs the capability, call [`invalidate`](../beprocesscapabilitygrant/invalidate.md) on the returned object.

## Parameters

- `capability`: The capability to grant.
- `error`: If an error occurs, upon return contains an [`NSError`](../../Foundation/nserror.md) object that describes the problem. If you don’t want information about errors that happen, pass in `NULL`.

## See Also

### Coordinating processes
- [- grantCapability:error:invalidationHandler:](./grantcapability_error_invalidationhandler_.md)
  Grants the specified capability to the process, invoking the handler when the capability becomes invalid.
- [- createVisibilityPropagationInteraction](./createvisibilitypropagationinteraction.md)
  Returns an interaction that associates a view with the web content process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentprocess/grantcapability:error:)*
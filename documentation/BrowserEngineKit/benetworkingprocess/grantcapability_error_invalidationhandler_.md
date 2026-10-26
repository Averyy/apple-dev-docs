# grantCapability:error:invalidationHandler:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Grants the specified capability to the process and observes an invalidation closure.

**Availability**:
- iOS 17.6+
- iPadOS 17.6+

## Declaration

```objc
- (id<BEProcessCapabilityGrant>) grantCapability:(BEProcessCapability *) capability error:(NSError **) error invalidationHandler:(void (^)()) invalidationHandler;
```

#### Return Value

A [`ProcessCapability.Grant`](../processcapability/grant.md) object that represents the granted capability.

#### Discussion

When the process no longer needs the capability, call [`invalidate()`](../processcapability/grant/invalidate%28%29.md) on the returned object.

## Parameters

- `capability`: The capability to grant.
- `invalidationHandler`: A closure that the system calls when the capability becomes invalid.

## See Also

### Coordinating processes
- [- grantCapability:error:](./grantcapability_error_.md)
  Grants the specified capability to the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/benetworkingprocess/grantcapability:error:invalidationhandler:)*
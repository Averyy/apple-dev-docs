# InvocationDecoder

**Framework**: Distributed  
**Kind**: associatedtype  
**Required**: Yes

Type of [`DistributedTargetInvocationDecoder`](distributedtargetinvocationdecoder.md) that should be used when decoding invocations during [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md) calls.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
associatedtype InvocationDecoder : DistributedTargetInvocationDecoder where Self.InvocationDecoder.SerializationRequirement == Self.InvocationEncoder.SerializationRequirement
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorsystem/invocationdecoder)*
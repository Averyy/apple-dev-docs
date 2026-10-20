# ResultHandler

**Framework**: Distributed  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of the result handler which will be offered the results returned by a distributed function invocation called via [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](./executedistributedtarget%28on,target,invocationdecoder,handler%29.md).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
associatedtype ResultHandler : DistributedTargetInvocationResultHandler
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorsystem/resulthandler)*
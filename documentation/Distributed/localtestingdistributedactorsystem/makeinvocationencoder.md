# makeInvocationEncoder()

**Framework**: Distributed  
**Kind**: method

Invoked by the Swift runtime when a distributed remote call is about to be made.

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
final func makeInvocationEncoder() -> LocalTestingDistributedActorSystem.InvocationEncoder
```

#### Discussion

The returned `DistributedTargetInvocation` will be populated with all arguments, generic substitutions, and specific error and return types that are associated with this specific invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem/makeinvocationencoder())*
# asLocalActor

**Framework**: Distributed  
**Kind**: property

Produces an erased `any Actor` reference to this known to be local distributed actor.

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
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
var asLocalActor: any Actor { get }
```

#### Discussion

Since this method is not distributed, it can only be invoked when the underlying distributed actor is known to be local, e.g. from a context that is isolated to this actor.

Such reference can be used to work with APIs accepting `isolated any Actor`, as only a local distributed actor can be isolated on and may be automatically erased to such `any Actor` when calling methods implicitly accepting the caller’s actor isolation, e.g. by using the `#isolation` macro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactor/aslocalactor)*
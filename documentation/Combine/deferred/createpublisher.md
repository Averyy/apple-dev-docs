# createPublisher

**Framework**: Combine  
**Kind**: property

The closure to execute when this deferred publisher receives a subscription.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let createPublisher: () -> DeferredPublisher
```

#### Discussion

The publisher returned by this closure immediately receives the incoming subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/deferred/createpublisher)*
# empty

**Framework**: Combine  
**Kind**: property

Returns the “empty” subscription.

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
static var empty: any Subscription { get }
```

#### Discussion

Use the empty subscription when you need a [`Subscription`](subscription.md) that ignores requests and cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscriptions/empty)*
# session

**Framework**: ARKit  
**Kind**: property

The session this view uses to provide coaching.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var session: ARSession? { get set }
```

#### Discussion

The coaching overlay monitors your app’s [`ARSession`](arsession.md) and reacts according to its tracking status. You don’t need to set this property if you set [`sessionProvider`](arcoachingoverlayview/sessionprovider.md) instead.

## See Also

- [var sessionProvider: (any ARSessionProviding)?](arcoachingoverlayview/sessionprovider.md)
  An object you designate that provides the current session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/session)*
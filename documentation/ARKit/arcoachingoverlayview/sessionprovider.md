# sessionProvider

**Framework**: ARKit  
**Kind**: property

An object you designate that provides the current session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@IBOutlet
@MainActor weak var sessionProvider: (any ARSessionProviding)? { get set }
```

#### Discussion

Use this property to set the coaching overlay’s [`session`](arcoachingoverlayview/session.md) when loading from a storyboard. If you set this property at runtime, the coaching overlay keeps its [`session`](arcoachingoverlayview/session.md) property up to date for you. If your app recreates its [`ARSession`](arsession.md) at any point, you may find it convienient to set the [`sessionProvider`](arcoachingoverlayview/sessionprovider.md) once rather than update the coaching overlay’s [`session`](arcoachingoverlayview/session.md) manually.

## See Also

- [var session: ARSession?](arcoachingoverlayview/session.md)
  The session this view uses to provide coaching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/sessionprovider)*
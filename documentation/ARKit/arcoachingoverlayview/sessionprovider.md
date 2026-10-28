# sessionProvider

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An object you designate that provides the current session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@IBOutlet
weak var sessionProvider: (any ARSessionProviding)? { get set }
```

```objc
@property (nonatomic, weak, nullable) NSObject<ARSessionProviding> * sessionProvider;
```

## Discussion

Use this property to set the coaching overlay’s [`session`](./session.md) when loading from a storyboard. If you set this property at runtime, the coaching overlay keeps its [`session`](./session.md) property up to date for you. If your app recreates its [`ARSession`](../arsession.md) at any point, you may find it convienient to set the [`sessionProvider`](./sessionprovider.md) once rather than update the coaching overlay’s [`session`](./session.md) manually.

## See Also

### Providing the Session
- [var session: ARSession?](./session.md)
  The session this view uses to provide coaching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/sessionprovider)*
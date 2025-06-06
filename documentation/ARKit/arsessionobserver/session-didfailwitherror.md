# session(_:didFailWithError:)

**Framework**: ARKit  
**Kind**: method

Tells the delegate that the session has stopped running due to an error.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func session(_ session: ARSession, didFailWithError error: any Error)
```

## Parameters

- `session`: The session providing information.
- `error`: An object describing the failure.

## See Also

- [let ARErrorDomain: String](arerrordomain.md)
  The domain for error objects produced by an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:didfailwitherror:))*
# session(_:didFailWithError:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the session has stopped running due to an error.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func session(_ session: ARSession, didFailWithError error: any Error)
```

```objc
- (void) session:(ARSession *) session didFailWithError:(NSError *) error;
```

## Parameters

- `session`: The session providing information.
- `error`: An object describing the failure.

## See Also

### Handling Errors
- [let ARErrorDomain: String](../arerrordomain.md)
  The domain for error objects produced by an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:didfailwitherror:))*
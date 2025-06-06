# authorizationViewReleasedAuthorization(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sent to the delegate to indicate that deauthorization is about to occur.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorizationViewReleasedAuthorization(_ view: SFAuthorizationView!)
```

#### Discussion

This method is called after deauthorization has been approved (either you called the [`deauthorize(_:)`](https://developer.apple.com/documentation/SecurityInterface/SFAuthorizationView/deauthorize(_:)) method, or the user clicked an open lock icon and the [`authorizationViewShouldDeauthorize(_:)`](nsobject-swift.class/authorizationviewshoulddeauthorize(_:).md) delegate method did not cancel the operation), and before the user is deauthorized (that is, before the [`authorizationViewDidDeauthorize(_:)`](nsobject-swift.class/authorizationviewdiddeauthorize(_:).md) delegate method is called).

## See Also

- [@MainActor func deauthorize(_ inSender: Any!) -> Bool](../SecurityInterface/SFAuthorizationView/deauthorize(_:).md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewreleasedauthorization(_:))*
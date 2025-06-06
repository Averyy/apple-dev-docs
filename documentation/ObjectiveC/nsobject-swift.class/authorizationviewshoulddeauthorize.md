# authorizationViewShouldDeauthorize(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sent to the delegate when a user clicks the open lock icon.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorizationViewShouldDeauthorize(_ view: SFAuthorizationView!) -> Bool
```

#### Discussion

The delegate can react to this before deauthorization happens and avoid it by returning [`NO`](no.md). This delegate method is not called when you call the [`deauthorize(_:)`](https://developer.apple.com/documentation/SecurityInterface/SFAuthorizationView/deauthorize(_:)) method.

## See Also

- [@MainActor func deauthorize(_ inSender: Any!) -> Bool](../SecurityInterface/SFAuthorizationView/deauthorize(_:).md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize(_:))*
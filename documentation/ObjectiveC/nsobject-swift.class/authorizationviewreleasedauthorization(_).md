# authorizationViewReleasedAuthorization(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate to indicate that deauthorization is about to occur.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorizationViewReleasedAuthorization(_ view: SFAuthorizationView!)
```

```objc
- (void) authorizationViewReleasedAuthorization:(SFAuthorizationView *) view;
```

## Discussion

This method is called after deauthorization has been approved (either you called the [`deauthorize(_:)`](../../SecurityInterface/sfauthorizationview/deauthorize%28_%29.md) method, or the user clicked an open lock icon and the [`authorizationViewShouldDeauthorize(_:)`](./authorizationviewshoulddeauthorize%28_%29.md) delegate method did not cancel the operation), and before the user is deauthorized (that is, before the [`authorizationViewDidDeauthorize(_:)`](./authorizationviewdiddeauthorize%28_%29.md) delegate method is called).

## See Also

### Related Documentation
- [func deauthorize(Any!) -> Bool](../../SecurityInterface/sfauthorizationview/deauthorize%28_%29.md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewreleasedauthorization(_:))*
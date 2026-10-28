# authorizationViewShouldDeauthorize(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when a user clicks the open lock icon.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorizationViewShouldDeauthorize(_ view: SFAuthorizationView!) -> Bool
```

```objc
- (BOOL) authorizationViewShouldDeauthorize:(SFAuthorizationView *) view;
```

## Discussion

The delegate can react to this before deauthorization happens and avoid it by returning [`NO`](../no.md). This delegate method is not called when you call the [`deauthorize(_:)`](../../SecurityInterface/sfauthorizationview/deauthorize%28_%29.md) method.

## See Also

### Related Documentation
- [func deauthorize(Any!) -> Bool](../../SecurityInterface/sfauthorizationview/deauthorize%28_%29.md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize(_:))*
# authorizationViewCreatedAuthorization(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate to indicate the authorization object has been created or changed.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorizationViewCreatedAuthorization(_ view: SFAuthorizationView!)
```

```objc
- (void) authorizationViewCreatedAuthorization:(SFAuthorizationView *) view;
```

## Discussion

If you have saved a copy of the authorization object for your own purposes, you should discard it and call [`authorization()`](../../SecurityInterface/sfauthorizationview/authorization%28%29.md) for a new authorization object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewcreatedauthorization(_:))*
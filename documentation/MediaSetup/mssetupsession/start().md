# start()

**Framework**: Media Setup  
**Kind**: method  
**Role**: Instance Method

Initiates the service configuration process and sends the account details of the streaming media service to the user’s HomePod speakers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func start() throws
```

```objc
- (BOOL) startWithError:(NSError **) error;
```

## See Also

### Presenting the Configuration View
- [var presentationContext: (any MSAuthenticationPresentationContext)?](./presentationcontext.md)
  A delegate that provides media setup display information to the system.
- [protocol MSAuthenticationPresentationContext](../msauthenticationpresentationcontext.md)
  A protocol that provides media setup display information to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediasetup/mssetupsession/start())*
# presentationContext

**Framework**: Media Setup  
**Kind**: property

A delegate that provides media setup display information to the system.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var presentationContext: (any MSAuthenticationPresentationContext)? { get set }
```

## See Also

- [protocol MSAuthenticationPresentationContext](msauthenticationpresentationcontext.md)
  A protocol that provides media setup display information to the system.
- [func start() throws](mssetupsession/start.md)
  Initiates the service configuration process and sends the account details of the streaming media service to the user’s HomePod speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediasetup/mssetupsession/presentationcontext)*
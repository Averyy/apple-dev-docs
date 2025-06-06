# MSAuthenticationPresentationContext

**Framework**: Media Setup  
**Kind**: protocol

A protocol that provides media setup display information to the system.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
protocol MSAuthenticationPresentationContext : NSObjectProtocol
```

## Topics

### Displaying the Media Setup View
- [func presentationAnchor() -> MSPresentationAnchor?](msauthenticationpresentationcontext/presentationanchor.md)
  A window that presents the system’s HomePod configuration view to the user.
- [typealias MSPresentationAnchor](mspresentationanchor.md)
  A window that presents a Media Setup configuration view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var presentationContext: (any MSAuthenticationPresentationContext)?](mssetupsession/presentationcontext.md)
  A delegate that provides media setup display information to the system.
- [func start() throws](mssetupsession/start.md)
  Initiates the service configuration process and sends the account details of the streaming media service to the user’s HomePod speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediasetup/msauthenticationpresentationcontext)*
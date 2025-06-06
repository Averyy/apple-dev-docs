# delegate

**Framework**: Multipeer Connectivity  
**Kind**: property

The delegate object that handles advertising-assistant-related events.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any MCAdvertiserAssistantDelegate)? { get set }
```

## See Also

- [init(serviceType: String, discoveryInfo: [String : String]?, session: MCSession)](mcadvertiserassistant/init(servicetype:discoveryinfo:session:).md)
  Initializes an advertiser assistant object.
- [var session: MCSession](mcadvertiserassistant/session.md)
  The session into which new peers are added after accepting an invitation.
- [var discoveryInfo: [String : String]?](mcadvertiserassistant/discoveryinfo.md)
  The `info` dictionary that was passed when this object was initialized.
- [var serviceType: String](mcadvertiserassistant/servicetype.md)
  The service type that your app is advertising.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/delegate)*
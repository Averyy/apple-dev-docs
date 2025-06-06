# init(serviceType:discoveryInfo:session:)

**Framework**: Multipeer Connectivity  
**Kind**: init

Initializes an advertiser assistant object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(serviceType: String, discoveryInfo info: [String : String]?, session: MCSession)
```

#### Return Value

An initialized instance, or `nil` if an error occurred.

#### Discussion

This method throws an exception if a valid `peerID` object is not provided, or if `serviceType` is not a legal Bonjour service type.

## Parameters

- `serviceType`: For more details, read  .
- `info`: If the data you need to provide is too large to fit within these constraints, create a custom discovery class using Bonjour for discovery and your choice of networking protocols for exchanging the information.
- `session`: The session into which new peers should be added after they accept the invitation.

## See Also

- [var session: MCSession](mcadvertiserassistant/session.md)
  The session into which new peers are added after accepting an invitation.
- [var delegate: (any MCAdvertiserAssistantDelegate)?](mcadvertiserassistant/delegate.md)
  The delegate object that handles advertising-assistant-related events.
- [var discoveryInfo: [String : String]?](mcadvertiserassistant/discoveryinfo.md)
  The `info` dictionary that was passed when this object was initialized.
- [var serviceType: String](mcadvertiserassistant/servicetype.md)
  The service type that your app is advertising.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/init(servicetype:discoveryinfo:session:))*
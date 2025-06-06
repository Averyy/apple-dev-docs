# Privacy Management

**Framework**: Network

Configure parameters related to user privacy.

## Topics

### Traffic Attribution
- [Inspecting app activity data](inspecting-app-activity-data.md)
  Verify that your app accesses only the user data and network resources that you expect it to access.
- [Indicating the source of network activity](indicating-the-source-of-network-activity.md)
  Control whether the App Privacy Report attributes network traffic to the app or to the user.
- [func nw_parameters_set_attribution(nw_parameters_t, nw_parameters_attribution_t)](nw_parameters_set_attribution(_:_:).md)
  Sets a flag that indicates whether the network request originates from the developer or the user.
- [func nw_parameters_get_attribution(nw_parameters_t) -> nw_parameters_attribution_t](nw_parameters_get_attribution(_:).md)
  Gets a flag that indicates whether the network request originates from the developer or the user.
- [enum nw_parameters_attribution_t](nw_parameters_attribution_t.md)
  The entities that can make a network request.

## See Also

- [Security Options](security-options.md)
  Configure security options for TLS handshakes.
- [Creating an Identity for Local Network TLS](creating-an-identity-for-local-network-tls.md)
  Learn how to create and use a digital identity in your application for local network TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/privacy-management)*
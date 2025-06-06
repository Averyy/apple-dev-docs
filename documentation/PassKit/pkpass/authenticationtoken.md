# authenticationToken

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The token for authenticating update requests.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var authenticationToken: String? { get }
```

#### Discussion

Use this property to store an authentication token for your web service. When the device requests an updated copy of the pass, the request’s header includes this authorization token. Use this token to verify that the request is from a valid device and not from an unauthorized source.

Don’t change the authentication token during an update.

## See Also

- [var webServiceURL: URL?](pkpass/webserviceurl.md)
  The URL for the web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/authenticationtoken)*
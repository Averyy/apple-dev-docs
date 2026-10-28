# additionalHeaderFields

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

Additional headers to send when loading the initial URL.

**Availability**:
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
var additionalHeaderFields: [String : String]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,NSString *> * additionalHeaderFields;
```

## Discussion

Apply these headers only to the initial page, and don’t overwrite any headers that the browser usually sends.

This example shows the call to the [`begin(_:)`](../aswebauthenticationsessionwebbrowsersessionhandling/begin%28_%29.md) delegate method when a web browser receives a request from an app. This implementation iterates over the additional header fields from the app’s request and adds them to its own request.

```swift
func begin(_ request: ASWebAuthenticationSessionRequest!) {
    self.request = request

    let urlRequest = URLRequest(url: request.url)
    // Use the new fields on the URL request.
    for (header, value) in request.additionalHeaderFields {
        urlRequest.addValue(value, forHTTPHeaderField: header)
    }

    // Load the URL request.
}
```

> ❗ **Important**: Your browser app needs to add `AdditionalHeaderFieldsAreSupported` with the value `YES` to the `ASWebAuthenticationSessionWebBrowserSupportCapabilities` dictionary in your app’s information property list to use this API. If the system doesn’t find this key in the default browser app, it sends the request to Safari instead.

## See Also

### Interpreting a request
- [var url: URL](./url.md)
  The web address the browser should use to perform the authentication request.
- [var shouldUseEphemeralSession: Bool](./shoulduseephemeralsession.md)
  A Boolean that indicates whether the browser should use a private browsing session.
- [var uuid: UUID](./uuid.md)
  A unique identifier for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/additionalheaderfields)*
# matchesURL(_:)

**Framework**: Authentication Services  
**Kind**: method

Checks whether a given URL matches the callback object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func matchesURL(_ url: URL) -> Bool
```

#### Discussion

Use this method in a browser app that adopts the `ASWebAuthenticationWebBrowser` API. Other apps can use it for debugging purposes.

The following example shows how a browser app’s internal method for determining redirect policies might use `matchesURL(_:)`:

```swift
// The pre-existing delegate method, which the system calls when the web browser receives a request from an app.
func begin(_ request: ASWebAuthenticationSessionRequest!) {
    self.request = request

    // Load the URL request.
}

// The web browser's internal method for determining redirect policies.
func myShouldNavigate(to url: URL) -> Bool {
    if request.callback.matches(url) {
        // Existing API to complete a request.
        request.complete(withCallbackURL: url)
    }
    ...
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/callback/matchesurl(_:))*
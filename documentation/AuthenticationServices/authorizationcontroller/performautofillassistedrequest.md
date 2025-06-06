# performAutoFillAssistedRequest(_:)

**Framework**: Authentication Services  
**Kind**: method

Performs an AutoFill-assisted authorization request.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performAutoFillAssistedRequest(_ request: ASAuthorizationRequest) async throws -> ASAuthorizationResult
```

#### Return Value

The request’s outcome. For more information, see [`ASAuthorizationResult`](asauthorizationresult.md).

#### Discussion

To perform AutoFill-assisted authorization requests, add the appropriate [`textContentType(_:)`](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)-ufdv) to any sign-in related fields, such as those for usernames and passwords:

```swift
TextField("Username", text: $username)
    .textContentType(.username)
```

Then use [`task(priority:_:)`](https://developer.apple.com/documentation/SwiftUI/View/task(priority:_:)) or [`task(id:priority:_:)`](https://developer.apple.com/documentation/SwiftUI/View/task(id:priority:_:)) to perform the request when the view appears:

```swift
.task {
    // Create the authorization request.
    async let request = makeAutoFillAuthorizationRequest()
    // Perform the request and await its result.
    let result = try await authorizationController
        .performAutoFillAssistedRequest(request)
    switch result {
        // Process the request's result.
    }
}
```

## Parameters

- `request`: The authorization request to perform.

## See Also

- [func performAutoFillAssistedRequests([ASAuthorizationRequest]) async throws -> ASAuthorizationResult](authorizationcontroller/performautofillassistedrequests(_:).md)
  Performs an AutoFill-assisted authorization request from the provided array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller/performautofillassistedrequest(_:))*
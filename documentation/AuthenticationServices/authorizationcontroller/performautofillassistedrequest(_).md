# performAutoFillAssistedRequest(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

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

The request’s outcome. For more information, see [`ASAuthorizationResult`](../asauthorizationresult.md).

#### Discussion

To perform AutoFill-assisted authorization requests, add the appropriate [`textContentType(_:)`](../../SwiftUI/view/textcontenttype%28_%29-ufdv.md) to any sign-in related fields, such as those for usernames and passwords:

```swift
TextField("Username", text: $username)
    .textContentType(.username)
```

Then use [`task(name:priority:file:line:_:)`](../../SwiftUI/view/task%28name,priority,file,line,_%29.md) or [`task(id:name:priority:file:line:_:)`](../../SwiftUI/view/task%28id,name,priority,file,line,_%29.md) to perform the request when the view appears:

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

### Performing assisted requests
- [func performAutoFillAssistedRequests([ASAuthorizationRequest]) async throws -> ASAuthorizationResult](./performautofillassistedrequests%28_%29.md)
  Performs an AutoFill-assisted authorization request from the provided array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller/performautofillassistedrequest(_:))*
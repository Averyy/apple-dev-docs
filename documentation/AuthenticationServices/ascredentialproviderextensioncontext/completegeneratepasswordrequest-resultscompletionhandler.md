# completeGeneratePasswordRequest(results:completionHandler:)

**Framework**: Authentication Services  
**Kind**: method

Return potential passwords for the given request.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
func completeGeneratePasswordRequest(results: [ASGeneratedPassword]) async -> Bool
```

## Parameters

- `results`: Potential passwords that the user can select. You can provide multiple options for increased flexibility on the user’s behalf.   These results should be returned in priority order.
- `completionHandler`: An optional block your extension can provide to perform any cleanup work after the system has captured the results.   The expired parameter is true if the system decides to prematurely end a previous non-expiration invocation of the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext/completegeneratepasswordrequest(results:completionhandler:))*
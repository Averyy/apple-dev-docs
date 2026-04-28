# completeRequest(withTextToInsert:completionHandler:)

**Framework**: Authentication Services  
**Kind**: method

Provides the user-selected text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
func completeRequest(withTextToInsert text: String) async -> Bool
```

#### Overview

At some point after you call this method, the system dismisses the associated view controller.

## Parameters

- `text`: The text to insert.
- `completionHandler`: Optional work that the extension performs as a background-priority task after the request completes. The `expired` parameter is `YES` if the system prematurely terminates a previous non-expiration invocation of the `completionHandler`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext/completerequest(withtexttoinsert:completionhandler:))*
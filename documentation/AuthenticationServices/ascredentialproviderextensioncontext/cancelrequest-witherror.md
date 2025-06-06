# cancelRequest(withError:)

**Framework**: Authentication Services  
**Kind**: method

Cancels the request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func cancelRequest(withError error: any Error)
```

## Mentions

- [Providing one-time passcodes to AutoFill](providing-one-time-passcodes-to-autofill.md)

#### Discussion

Call this method if the user cancels the action or if a failure occurs. The system dismisses your extension’s view controller automatically.

## Parameters

- `error`: Use an error domain of   and a code of type  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext/cancelrequest(witherror:))*
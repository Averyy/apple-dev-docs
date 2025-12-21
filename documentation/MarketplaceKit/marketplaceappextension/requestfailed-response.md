# requestFailed(response:)

**Framework**: MarketplaceKit  
**Kind**: method  
**Required**: Yes

Handles when the operating system receives an unexpected response from your web server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func requestFailed(response: HTTPURLResponse) async -> Bool
```

## Mentions

- [Reauthenticating a person to manage apps](reauthenticating-a-person-to-manage-apps.md)
- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)

#### Discussion

iOS invokes your implementation of this callback when it receives anything but an OK status from your marketplace endpoints. Your implementation performs the necessary action according to the given status code. Your server might be down or it might return a code that indicates that the person needs to reauthenticate, if for example, their access token expires.

For more information, see [`Installing apps from an alternative marketplace`](installing-apps-from-an-alternative-marketplace.md).

## Parameters

- `response`: An object that contains details of the response, such as the status code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplaceappextension/requestfailed(response:))*
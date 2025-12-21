# additionalHeaders(for:account:)

**Framework**: MarketplaceKit  
**Kind**: method  
**Required**: Yes

Adds information to the request header for communications from the operating system to your marketplace endpoints.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func additionalHeaders(for request: URLRequest, account: String) async -> [String : String]
```

## Mentions

- [Reauthenticating a person to manage apps](reauthenticating-a-person-to-manage-apps.md)
- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)

#### Discussion

The operating system invokes your implementation of this callback before sending a request to your marketplace endpoints. In this method, use [`addValue(_:forHTTPHeaderField:)`](https://developer.apple.com/documentation/Foundation/URLRequest/addValue(_:forHTTPHeaderField:)) to add to the header. The additions detail information that your marketplace server needs to authorize the request.

For more information, see [`Installing apps from an alternative marketplace`](installing-apps-from-an-alternative-marketplace.md).

## Parameters

- `request`: A request that contains a header to which you add information.
- `account`: Authentication information about the signed-in person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplaceappextension/additionalheaders(for:account:))*
# attribution

**Framework**: Foundation  
**Kind**: property

The entity that initiates the network request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var attribution: URLRequest.Attribution { get set }
```

#### Discussion

If you don’t set this value, the system assumes a value of [`NSURLRequest.Attribution.developer`](nsurlrequest/attribution-swift.enum/developer.md). Use this default value for any network request that your app makes that isn’t explicitly from the user. This includes requests that you make to your own server, even when you load user data. It also includes links that the user selects, but that you modify in any way — including by adding HTTP headers — before loading the content.

Set this value to [`NSURLRequest.Attribution.user`](nsurlrequest/attribution-swift.enum/user.md) only for requests that the user explicitly makes, like when the user enters a URL or taps or clicks a URL that they can read, and only if your app loads and displays the data without altering the request.

## See Also

- [URLRequest.Attribution](urlrequest/attribution-swift.typealias.md)
  A type that indicates the entities that can make a network request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/attribution-swift.property)*
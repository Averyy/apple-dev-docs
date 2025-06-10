# NSURLRequest.Attribution.developer

**Framework**: Foundation  
**Kind**: case

A developer-initiated network request.

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
case developer
```

#### Discussion

Use this value for the [`attribution`](urlrequest/attribution-swift.property.md) parameter of a URL request that your app makes for any purpose other than when the user explicitly accesses a link. This includes requests that your app makes to get user data. This is the default value.

For cases where the user enters a URL, like in the navigation bar of a web browser, or taps or clicks a URL to load the content it represents, use the [`NSURLRequest.Attribution.user`](nsurlrequest/attribution-swift.enum/user.md) value instead.

## See Also

- [NSURLRequest.Attribution.user](nsurlrequest/attribution-swift.enum/user.md)
  The user explicitly directs the app to make a network request.
- [NSURLRequest.Attribution.user](nsurlrequest/attribution-swift.enum/user.md)
  The user explicitly directs the app to make a network request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/attribution-swift.enum/developer)*
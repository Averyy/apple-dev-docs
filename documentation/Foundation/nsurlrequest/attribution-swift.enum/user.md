# NSURLRequest.Attribution.user

**Framework**: Foundation  
**Kind**: case

The user explicitly directs the app to make a network request.

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
case user
```

#### Discussion

Use this value for the [`attribution`](urlrequest/attribution-swift.property.md) parameter of a URL request that satisfies a user request to access an explicit, unmodified URL. In all other cases, use the [`NSURLRequest.Attribution.developer`](nsurlrequest/attribution-swift.enum/developer.md) value instead.

## See Also

- [NSURLRequest.Attribution.developer](nsurlrequest/attribution-swift.enum/developer.md)
  A developer-initiated network request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/attribution-swift.enum/user)*
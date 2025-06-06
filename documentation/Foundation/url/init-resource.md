# init(resource:)

**Framework**: Foundation  
**Kind**: init

Creates a URL from a resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init?(resource: URLResource)
```

#### Discussion

Use this initializer to resolve [`URLResource`](urlresource.md) instances, possibly received from other processes, into [`URL`](url.md) instances.

## Parameters

- `resource`: A   that provides a reference to a resource in a given bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(resource:))*
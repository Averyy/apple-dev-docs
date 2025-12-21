# requestIsCacheEquivalent(_:to:)

**Framework**: Foundation  
**Kind**: method

A Boolean value indicating whether two requests are equivalent for cache purposes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func requestIsCacheEquivalent(_ a: URLRequest, to b: URLRequest) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `aRequest` and `bRequest` are equivalent for cache purposes, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

Requests are considered equivalent for cache purposes if and only if they would be handled by the same protocol and that protocol declares them equivalent after performing implementation-specific checks.

The [`URLProtocol`](urlprotocol.md) implementation of this method compares the URLs of the requests to determine if the requests should be considered equivalent. Subclasses can override this method to provide protocol-specific comparisons.

## Parameters

- `a`: The request to compare with  .
- `b`: The request to compare with  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/requestiscacheequivalent(_:to:))*
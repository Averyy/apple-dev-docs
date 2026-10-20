# appending(queryItems:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new URL formed by appending a list of query items to the URL.

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
func appending(queryItems: [URLQueryItem]) -> URL
```

## Parameters

- `queryItems`: An array of [`URLQueryItem`](../urlqueryitem.md) instances to append to the URL.

## See Also

### Adding query items
- [func append(queryItems: [URLQueryItem])](./append%28queryitems%29.md)
  Appends a list of query items to the URL.
- [struct URLQueryItem](../urlqueryitem.md)
  A single name-value pair from the query portion of a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appending(queryitems:))*
# makeBody(configuration:)

**Framework**: StoreKit  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a product view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration`: The properties of a product view style.

## See Also

- [ProductViewStyle.Configuration](productviewstyle/configuration.md)
  A type that represents the properties of a product view style.
- [associatedtype Body : View](productviewstyle/body.md)
  A view that represents the body of a product view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/productviewstyle/makebody(configuration:))*
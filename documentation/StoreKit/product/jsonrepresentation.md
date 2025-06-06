# jsonRepresentation

**Framework**: StoreKit  
**Kind**: property

The JSON representation of the product information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var jsonRepresentation: Data { get }
```

#### Discussion

The [`jsonRepresentation`](product/jsonrepresentation.md) is UTF-8 string data. You can use the JSON data to decode the product information into your own data type instead of using the [`Product`](product.md) value directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/jsonrepresentation)*
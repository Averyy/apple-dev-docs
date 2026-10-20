# buyProduct(identifier:options:)

**Framework**: StoreKit Test  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@discardableResult
func buyProduct(identifier: Product.ID, options: Set<Product.PurchaseOption> = []) async throws -> Transaction
```

## See Also

- [func setSimulatedError<API>(API.Failure?, forAPI: API) async throws](sktestsession/setsimulatederror(_:forapi:).md)
- [func simulatedError<API>(forAPI: API) async -> API.Failure?](sktestsession/simulatederror(forapi:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/buyproduct(identifier:options:))*
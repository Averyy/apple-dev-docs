# buyProduct(identifier:options:)

**Framework**: StoreKit Test  
**Kind**: method  
**Role**: Instance Method

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

### Instance Methods
- [func setSimulatedError<API>(API.Failure?, forAPI: API) async throws](./setsimulatederror%28_,forapi%29.md)
- [func simulatedError<API>(forAPI: API) async -> API.Failure?](./simulatederror%28forapi%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/buyproduct(identifier:options:))*
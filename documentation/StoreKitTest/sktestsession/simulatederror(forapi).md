# simulatedError(forAPI:)

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
func simulatedError<API>(forAPI api: API) async -> API.Failure? where API : FailableStoreKitAPI
```

## See Also

### Instance Methods
- [func buyProduct(identifier: Product.ID, options: Set<Product.PurchaseOption>) async throws -> Transaction](./buyproduct%28identifier,options%29.md)
- [func setSimulatedError<API>(API.Failure?, forAPI: API) async throws](./setsimulatederror%28_,forapi%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/simulatederror(forapi:))*
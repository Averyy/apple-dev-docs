# next(isolation:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

**Availability**:
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)

## Declaration

```swift
func next(isolation actor: isolated (any Actor)?) async throws(ManagedPackageLibrary.ManagedPackages.AsyncIterator.Failure) -> ManagedPackageLibrary.ManagedPackages.AsyncIterator.Element?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedpackagelibrary/managedpackages/asynciterator/next(isolation:))*
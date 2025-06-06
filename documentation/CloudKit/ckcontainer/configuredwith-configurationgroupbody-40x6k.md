# configuredWith(configuration:group:body:)

**Framework**: CloudKit  
**Kind**: method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
@discardableResult
func configuredWith<R>(configuration: CKOperation.Configuration? = nil, group: CKOperationGroup? = nil, body: (CKContainer) throws -> R) rethrows -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/configuredwith(configuration:group:body:)-40x6k)*
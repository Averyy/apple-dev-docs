# AppStore.Environment

**Framework**: StoreKit  
**Kind**: struct

Constants that represent the App Store server environment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Environment
```

## Topics

### Getting the environment value
- [static let production: AppStore.Environment](appstore/environment/production.md)
  A value that indicates the production server environment.
- [static let sandbox: AppStore.Environment](appstore/environment/sandbox.md)
  A value that indicates the sandbox server environment.
- [static let xcode: AppStore.Environment](appstore/environment/xcode.md)
  A value that indicates the StoreKit Testing in Xcode environment.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let environment: AppStore.Environment](apptransaction/environment.md)
  The server environment that signs the app transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/environment)*
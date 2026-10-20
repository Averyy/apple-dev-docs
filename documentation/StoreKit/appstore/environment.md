# AppStore.Environment

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Constants that represent the App Store server environment.

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
struct Environment
```

## Topics

### Getting the environment value
- [static let production: AppStore.Environment](./environment/production.md)
  A value that indicates the production server environment.
- [static let sandbox: AppStore.Environment](./environment/sandbox.md)
  A value that indicates the sandbox server environment.
- [static let xcode: AppStore.Environment](./environment/xcode.md)
  A value that indicates the StoreKit Testing in Xcode environment.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the environment
- [let environment: AppStore.Environment](../apptransaction/environment.md)
  The server environment that signs the app transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore/environment)*
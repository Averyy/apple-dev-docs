# AppTransaction.StoreType

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Values that identify the store where the original purchase of an app took place.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct StoreType
```

## Topics

### Getting store types
- [static let consumer: AppTransaction.StoreType](./storetype-swift.struct/consumer.md)
  A value that indicates the App Store.
- [static let enterprise: AppTransaction.StoreType](./storetype-swift.struct/enterprise.md)
  A value that indicates Apple Business.
- [static let education: AppTransaction.StoreType](./storetype-swift.struct/education.md)
  A value that indicates Apple School Manager.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the store
- [let storeType: AppTransaction.StoreType](./storetype-swift.property.md)
  The store where the original purchase of the app took place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/storetype-swift.struct)*
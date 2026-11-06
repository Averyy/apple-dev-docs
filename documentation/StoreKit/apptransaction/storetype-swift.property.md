# storeType

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The store where the original purchase of the app took place.

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
let storeType: AppTransaction.StoreType
```

## Mentions

- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)

## Discussion

The value is [`consumer`](./storetype-swift.struct/consumer.md) for apps from the App Store. It’s [`enterprise`](./storetype-swift.struct/enterprise.md) or [`education`](./storetype-swift.struct/education.md) for apps that an organization gets through Apple Business or Apple School Manager.

A customer who has access to a subscription through a group gets the app from the App Store, so the store type doesn’t indicate group membership. To find out how a customer has access to a subscription, check the transaction’s [`ownershipType`](../transaction/ownershiptype-swift.property.md).

For more information, see [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md).

## See Also

### Getting the store
- [AppTransaction.StoreType](./storetype-swift.struct.md)
  Values that identify the store where the original purchase of an app took place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/storetype-swift.property)*
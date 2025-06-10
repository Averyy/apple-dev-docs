# querySubscriptionOptions

**Framework**: CloudKit  
**Kind**: property

Options that define the behavior of the subscription.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var querySubscriptionOptions: CKQuerySubscription.Options { get }
```

#### Discussion

Set the value of this property at initialization time. When you configure a query-based subscription, use one of the following values:

- [`firesOnRecordCreation`](ckquerysubscription/options/firesonrecordcreation.md)
- [`firesOnRecordUpdate`](ckquerysubscription/options/firesonrecordupdate.md)
- [`firesOnRecordDeletion`](ckquerysubscription/options/firesonrecorddeletion.md)

If you don’t set an option, the system throws an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException).

## See Also

- [var predicate: NSPredicate](ckquerysubscription/predicate.md)
  The matching criteria to apply to records.
- [CKQuerySubscription.Options](ckquerysubscription/options.md)
  Configuration options for a query subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/querysubscriptionoptions)*
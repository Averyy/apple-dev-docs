# DefaultHistoryToken

**Framework**: SwiftData  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
struct DefaultHistoryToken
```

## Topics

### Instance Properties
- [var storeIdentifier: String](./defaulthistorytoken/storeidentifier.md)
  The on-disk identifier of the data store this token covers (SD-0028).

## Relationships

### Conforms To
- [Comparable](../Swift/comparable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [HistoryToken](./historytoken.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### History life cycle
- [enum HistoryChange](./historychange.md)
  Values that describe data history transactions.
- [protocol HistoryDelete](./historydelete.md)
  An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [protocol HistoryInsert](./historyinsert.md)
- [protocol HistoryToken](./historytoken.md)
- [protocol HistoryTransaction](./historytransaction.md)
- [protocol HistoryUpdate](./historyupdate.md)
- [struct HistoryTombstone](./historytombstone.md)
- [struct DefaultHistoryInsert](./defaulthistoryinsert.md)
- [struct DefaultHistoryUpdate](./defaulthistoryupdate.md)
- [struct DefaultHistoryDelete](./defaulthistorydelete.md)
- [struct DefaultHistoryTransaction](./defaulthistorytransaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaulthistorytoken)*
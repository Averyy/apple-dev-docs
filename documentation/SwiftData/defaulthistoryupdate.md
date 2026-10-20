# DefaultHistoryUpdate

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
struct DefaultHistoryUpdate<Model> where Model : PersistentModel
```

## Topics

### Operators
- [static func == (DefaultHistoryUpdate<Model>, DefaultHistoryUpdate<Model>) -> Bool](./defaulthistoryupdate/eqeq%28_,_%29.md)
### Instance Methods
- [func hash(into: inout Hasher)](./defaulthistoryupdate/hash%28into%29.md)
### Type Aliases
- [DefaultHistoryUpdate.PropertyUpdate](./defaulthistoryupdate/propertyupdate.md)

## Relationships

### Conforms To
- [HistoryUpdate](./historyupdate.md)
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
- [struct DefaultHistoryDelete](./defaulthistorydelete.md)
- [struct DefaultHistoryToken](./defaulthistorytoken.md)
- [struct DefaultHistoryTransaction](./defaulthistorytransaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaulthistoryupdate)*
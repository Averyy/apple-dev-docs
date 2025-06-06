# DefaultHistoryUpdate

**Framework**: SwiftData  
**Kind**: struct

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
- [static func == (DefaultHistoryUpdate<Model>, DefaultHistoryUpdate<Model>) -> Bool](defaulthistoryupdate/==(_:_:).md)
### Instance Properties
- [let changeIdentifier: DefaultHistoryUpdate<Model>.ChangeIdentifier](defaulthistoryupdate/changeidentifier-swift.property.md)
- [let changedPersistentIdentifier: PersistentIdentifier](defaulthistoryupdate/changedpersistentidentifier.md)
- [let transactionIdentifier: DefaultHistoryUpdate<Model>.TransactionIdentifier](defaulthistoryupdate/transactionidentifier-swift.property.md)
- [let updatedAttributes: [any PartialKeyPath<Model> & Sendable]](defaulthistoryupdate/updatedattributes.md)
### Instance Methods
- [func hash(into: inout Hasher)](defaulthistoryupdate/hash(into:).md)
### Type Aliases
- [DefaultHistoryUpdate.ChangeIdentifier](defaulthistoryupdate/changeidentifier-swift.typealias.md)
- [DefaultHistoryUpdate.PropertyUpdate](defaulthistoryupdate/propertyupdate.md)
- [DefaultHistoryUpdate.TransactionIdentifier](defaulthistoryupdate/transactionidentifier-swift.typealias.md)

## Relationships

### Conforms To
- [HistoryUpdate](historyupdate.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaulthistoryupdate)*
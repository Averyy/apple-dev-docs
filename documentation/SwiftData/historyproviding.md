# HistoryProviding

**Framework**: SwiftData  
**Kind**: protocol

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
protocol HistoryProviding
```

## Topics

### Associated Types
- [associatedtype HistoryType : HistoryTransaction](historyproviding/historytype-swift.associatedtype.md)
### Instance Methods
- [func deleteHistory(HistoryDescriptor<Self.HistoryType>) throws](historyproviding/deletehistory(_:).md)
- [func fetchHistory(HistoryDescriptor<Self.HistoryType>) throws -> [Self.HistoryType]](historyproviding/fetchhistory(_:).md)
### Type Properties
- [static var historyType: Self.HistoryType.Type](historyproviding/historytype-swift.type.property.md)

## Relationships

### Conforming Types
- [DefaultStore](defaultstore.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyproviding)*
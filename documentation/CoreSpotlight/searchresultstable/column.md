# SearchResultsTable.Column

**Framework**: Core Spotlight  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Column
```

## Topics

### Initializers
- [init(name: String, type: SearchResultsTable.ValueType)](searchresultstable/column/init(name:type:).md)
### Instance Properties
- [let name: String](searchresultstable/column/name.md)
- [let type: SearchResultsTable.ValueType](searchresultstable/column/type.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let header: String?](searchresultstable/header.md)
  What this table represents (e.g., “Emails per month from John”).
- [let columns: [SearchResultsTable.Column]](searchresultstable/columns.md)
  Column definitions with name and type hint.
- [let rows: [SearchResultsTable.Row]](searchresultstable/rows.md)
  Data rows — each row’s values array matches `columns` by index.
- [SearchResultsTable.Row](searchresultstable/row.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchresultstable/column)*
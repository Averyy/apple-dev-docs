# SearchResultsTable.Column

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Column
```

## Topics

### Initializers
- [init(name: String, type: SearchResultsTable.ValueType)](./column/init%28name,type%29.md)
### Instance Properties
- [let name: String](./column/name.md)
- [let type: SearchResultsTable.ValueType](./column/type.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the column and row details
- [let header: String?](./header.md)
  What this table represents (e.g., “Emails per month from John”).
- [let columns: [SearchResultsTable.Column]](./columns.md)
  Column definitions with name and type hint.
- [let rows: [SearchResultsTable.Row]](./rows.md)
  Data rows — each row’s values array matches `columns` by index.
- [SearchResultsTable.Row](./row.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchresultstable/column)*
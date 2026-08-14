# SearchResultsTable.Row

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
struct Row
```

## Topics

### Initializers
- [init(values: [SearchResultsTable.Value])](searchresultstable/row/init(values:).md)
### Instance Properties
- [let values: [SearchResultsTable.Value]](searchresultstable/row/values.md)

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
- [SearchResultsTable.Column](searchresultstable/column.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchresultstable/row)*
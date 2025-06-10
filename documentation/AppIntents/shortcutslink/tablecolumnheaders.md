# tableColumnHeaders(_:)

**Framework**: App Intents  
**Kind**: method

Controls the visibility of a `Table`’s column header views.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func tableColumnHeaders(_ visibility: Visibility) -> some View
```

#### Discussion

By default, `Table` will display a global header view with the labels of each table column. This area is also where users can sort, resize, and rearrange the columns. For simple cases that don’t require those features, this header can be hidden.

This will not affect the header of any `Section`s in a table.

```swift
Table(article.authors) {
    TableColumn("Name", value: \.name)
    TableColumn("Title", value: \.title)
}
.tableColumnHeaders(.hidden)
```

## Parameters

- `visibility`: A value of   will show table columns,    will remove them, and   will defer to default   behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/tablecolumnheaders(_:))*
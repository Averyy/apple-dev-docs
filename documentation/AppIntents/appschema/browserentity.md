# AppSchema.BrowserEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the browser domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol BrowserEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var bookmark: some AppSchemaEntity](./browserentity/bookmark.md)
  An entity schema for a bookmark.
- [var readingListItem: some AppSchemaEntity](./browserentity/readinglistitem.md)
  An entity schema for a reading list item.
- [var tab: some AppSchemaEntity](./browserentity/tab.md)
  An entity schema for a tab.
- [var tabGroup: some AppSchemaEntity](./browserentity/tabgroup.md)
  An entity schema for a tab group.
- [var window: some AppSchemaEntity](./browserentity/window.md)
  An entity schema for a window.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var bookmark: some AppSchemaEntity](./browserentity/bookmark.md)
  An entity schema for a bookmark.
- [var readingListItem: some AppSchemaEntity](./browserentity/readinglistitem.md)
  An entity schema for a reading list item.
- [var tab: some AppSchemaEntity](./browserentity/tab.md)
  An entity schema for a tab.
- [var tabGroup: some AppSchemaEntity](./browserentity/tabgroup.md)
  An entity schema for a tab group.
- [var window: some AppSchemaEntity](./browserentity/window.md)
  An entity schema for a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/browserentity)*
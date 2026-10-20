# MarkupID

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

An opaque ID for markup elements.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct MarkupID<Element>
```

## Topics

### Creating an ID
- [init()](./markupid/init%28%29.md)
  Creates a new unique ID.
### Converting IDs
- [MarkupOrderedSet.ElementID](./markuporderedset/elementid.md)
  The markup ID types supported in a markup ordered set.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data model
- [struct PaperMarkup](./papermarkup.md)
  The data model object for storing markup data created from a `PaperViewController`.
- [struct MarkupOrderedSet](./markuporderedset.md)
  An ordered set of markup elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupid)*
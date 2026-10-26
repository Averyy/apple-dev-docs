# Addition

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

Properties that all addition types share.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Addition
```

#### Discussion

This is an abstract definition. Don’t use this object type directly; use only the objects that extend it, such as [`LinkAddition`](./linkaddition.md).

## Properties

- `type` (string) *(required)*: The type of addition. For example, [`LinkAddition`](./linkaddition.md).

  **Allowed Values**: `link`, `calendar_event`
- `rangeLength` (integer): The number of text characters to highlight in the link.
- `rangeStart` (integer): The starting character index for which the addition is meant. A range starts at `0` for the first character.

  If you specify `rangeStart`, you must also specify `rangeLength`.

## Relationships

### Inherited By
- [LinkAddition](./linkaddition.md)

## See Also

### Links
- [object LinkAddition](./linkaddition.md)
  The addition object for defining links in text components that don’t use HTML or Markdown formatting.
- [object ComponentLink](./componentlink.md)
  The component addition object for making a component interactive and opening a link to another location in News.
- [object ComponentAddition](./componentaddition.md)
  Properties that all types of component additions share.
- [type SupportedURLs](./supportedurls.md)
  Links that go to Apple News, other Apple apps, and external sites.
- [type SupportedInternalURLs](./supportedinternalurls.md)
  Links that go to Apple News and other Apple apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/addition)*
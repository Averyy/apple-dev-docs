# ComponentAddition

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

Properties that all types of component additions share.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ComponentAddition
```

#### Discussion

Don’t use this object type directly; use only the objects that extend it, like [`ComponentLink`](./componentlink.md).

## Properties

- `type` (string) *(required)*: The type of component addition; for example [`ComponentLink`](./componentlink.md).

  **Allowed Values**: `link`, `calendar_event`

## Relationships

### Inherited By
- [ComponentLink](./componentlink.md)

## See Also

### Links
- [object LinkAddition](./linkaddition.md)
  The addition object for defining links in text components that don’t use HTML or Markdown formatting.
- [object ComponentLink](./componentlink.md)
  The component addition object for making a component interactive and opening a link to another location in News.
- [object Addition](./addition.md)
  Properties that all addition types share.
- [type SupportedURLs](./supportedurls.md)
  Links that go to Apple News, other Apple apps, and external sites.
- [type SupportedInternalURLs](./supportedinternalurls.md)
  Links that go to Apple News and other Apple apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/componentaddition)*
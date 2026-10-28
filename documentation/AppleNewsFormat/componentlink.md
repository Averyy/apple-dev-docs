# ComponentLink

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component addition object for making a component interactive and opening a link to another location in News.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ComponentLink
```

## Discussion

Use the `ComponentLink` object to define a link for a component by specifying the URL. Apple News ignores links that it can’t resolve to a valid entity.

You can use this object in [`Aside`](./aside.md), [`Chapter`](./chapter.md), [`Container`](./container.md), [`Logo`](./logo.md), [`Image`](./image.md), and [`Section`](./section.md).

### Example

```json
{
  "components": [
    {
      "role": "image",
      "URL": "bundle://image.jpg",
      "additions": [
        {
          "type": "link",
          "URL": "https://apple.news/TqT-jfrI0QXaYqGoz68HYeQ"
        }
      ]
    }
  ]
}
```

## Properties

- `URL` (SupportedInternalURLs) *(required)*: The URL to open when someone interacts with the component.
- `type` (string) *(required)*: The type of addition. Use `link`.

  **Allowed Values**: `link`

## Relationships

### Inherits From
- [ComponentAddition](./componentaddition.md)

## See Also

### Links
- [object LinkAddition](./linkaddition.md)
  The addition object for defining links in text components that don’t use HTML or Markdown formatting.
- [object Addition](./addition.md)
  Properties that all addition types share.
- [object ComponentAddition](./componentaddition.md)
  Properties that all types of component additions share.
- [type SupportedURLs](./supportedurls.md)
  Links that go to Apple News, other Apple apps, and external sites.
- [type SupportedInternalURLs](./supportedinternalurls.md)
  Links that go to Apple News and other Apple apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/componentlink)*
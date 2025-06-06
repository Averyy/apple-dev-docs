# Context.Metadata

**Framework**: ClassKit Catalog API  
**Kind**: dictionary

Information that helps the system categorize a context.

**Availability**:
- ClassKit 1.0+

## Declaration

```swift
object Context.Metadata
```

## Mentions

- [Preparing Context Data](preparing-context-data.md)

#### Discussion

You typically design a context with a specific locale in mind, and use the `locale` field to indicate that locale. However, you may want to make the context available in other locales. For example, a context that you design for the `en-us` locale may be suitable for any English-speaking locale, like `en-gb`, `en-au`, and so on. Use the `presentableLocales` field to indicate all the locales for which you consider the content to be suitable. Use a single-element array with the value `mul` to indicate suitability for any locale.

If you create multiple contexts to represent the same content for different locales, be sure that the set of presentable locales for one context doesn’t overlap the set of presentable locales for others. This might result in teachers seeing multiple versions of the same content. For example, if you use `mul` for one context’s presentable values, and `en-us` for a second, Schoolwork presents an English-speaking teacher in the United States with both contexts, as if they represent different content.

## Topics

### Parent Contexts
- [object Context.Metadata.PresentablePaths](context/metadata-data.dictionary/presentablepaths-data.dictionary.md)
  The identifier path of a context to use as one of the presentable paths in a context’s metadata.

## See Also

- [object Context.Data](context/data-data.dictionary.md)
  The data that makes up a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/context/metadata-data.dictionary)*
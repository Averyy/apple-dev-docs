# Component

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

Properties shared by all component types.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Component
```

## Discussion

In Apple News Format, every component has a property named `role` that conveys the component’s semantic value and its function in the article. For example, a `role` property that has a value of `body` indicates a `body` component, which means that its content is part of the article’s body text. A component whose `role` property has a value of `photo` represents one of the images in the article.

> ❗ **Important**:  Don’t use this object type directly. Instead, use objects (such as `author,` `title`, `figure`, and so on) that extend the `Component` object.

You can use this object in [`ArticleDocument`](./articledocument.md) and [`Container`](./container.md).

## Properties

- `role` (string) *(required)*: The `role` of a component (for example, `title`, `body`, or `pullquote`) conveys the semantic value of the content or its function within the article.

  The value of the `role` property is simply the `role` name; it doesn’t include the actual content that the role describes. For example, a `role` with the value `pullquote` describes a `text` component whose value is the actual pull quote text.

  A `role` can have design significance: Apple News Format derives styling and layout from it.  VoiceOver also uses the role to make Apple News content more accessible.

  For a list of valid component types, see [Components](../AppleNews/components.md).
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation  the component applies.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): A unique identifier for this component. If you use `identifier`, it must be unique across the entire document. Apple News Format requires an identifier if you want to anchor other components to this component.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` you define at the top level of the document.

  If you don’t define `layout`, Apple News Format bases the size and position on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherited By
- [ARKit](./arkit.md)
- [ArticleThumbnail](./articlethumbnail.md)
- [Audio](./audio.md)
- [BannerAdvertisement](./banneradvertisement.md)
- [Container](./container.md)
- [DataTable](./datatable.md)
- [Divider](./divider.md)
- [EmbedWebVideo](./embedwebvideo.md)
- [FacebookPost](./facebookpost.md)
- [Figure](./figure.md)
- [FlexibleSpacer](./flexiblespacer.md)
- [Gallery](./gallery.md)
- [HTMLTable](./htmltable.md)
- [Image](./image.md)
- [Instagram](./instagram.md)
- [LinkButton](./linkbutton.md)
- [Logo](./logo.md)
- [Map](./map.md)
- [MediumRectangleAdvertisement](./mediumrectangleadvertisement.md)
- [Mosaic](./mosaic.md)
- [Music](./music.md)
- [Photo](./photo.md)
- [Place](./place.md)
- [Podcast](./podcast.md)
- [Portrait](./portrait.md)
- [ReplicaAdvertisement](./replicaadvertisement.md)
- [Text](./text.md)
- [TikTok](./tiktok.md)
- [Tweet](./tweet.md)
- [Video](./video.md)

## See Also

### First Steps
- [Adding Components](../AppleNews/adding-components.md)
  Learn the basics for adding components to your article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/component)*
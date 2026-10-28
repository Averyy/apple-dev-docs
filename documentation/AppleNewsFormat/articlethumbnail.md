# ArticleThumbnail

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for displaying a thumbnail image with an article link.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object ArticleThumbnail
```

## Mentions

- [Creating an Article Link](../AppleNews/creating-an-article-link.md)
- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

## Discussion

Use the `ArticleThumbnail` object to display the thumbnail of an article. Use this component inside an [`ArticleLink`](./articlelink.md) component. The value of the `URL` property is automatically populated to reference the thumbnail image associated with the article (using the `articleIdentifier` property of the `ArticleLink` component). To provide a custom thumbnail, use another component, such as [`Image`](./image.md).

### Example

```json
{
  "components": [
    {
      "role": "article_link",
      "articleIdentifier": "https://apple.news/AT6kNQslCQy6EE4bF8hpOoQ",
      "components": [
        {
          "role": "article_thumbnail",
          "aspectRatio": 1,
          "fillMode": "cover",
          "verticalAlignment": "top"
        },
        {
          "role": "article_title"
        }
      ]
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `article_thumbnail` for this component.

  **Allowed Values**: `article_thumbnail`
- `accessibilityCaption` (string): A caption that describes the image. VoiceOver uses this text. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
- `additions` ([ComponentLink]): Ignored for all subcomponents of [`ArticleLink`](./articlelink.md).
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `articleIdentifier` (string): The identifier of the article that this component displays the thumbnail of. By default the `articleIdentifier` value is inherited from the [`ArticleLink`](./articlelink.md) component.
- `aspectRatio` (float) *(deprecated)*: The aspect ratio of the component in which the article thumbnail is displayed.

  **Default**: `1`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [Springy](https://developer.apple.com/library/archive/documentation/General/Conceptual/Apple_News_Format_Ref/SpringyBehavior.html#//apple_ref/doc/uid/TP40015408-CH73).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `caption` ((CaptionDescriptor | string)): A caption that describes the image. The article displays this text when the image is full screen, and VoiceOver uses this text if you don’t provide `accessibilityCaption` text. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. The caption text doesn’t appear in the main article view. To display a caption in the main article view, use the [`Caption`](./caption.md) component.

  **Allowed Types**: `CaptionDescriptor`, `string`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `explicitContent` (boolean): A Boolean that indicates that the image may contain explicit content.
- `fillMode` (string) *(deprecated)*: A string that indicates how to display the image fill.

  Valid values:

  - `cover` (default). Scales the image by aspect ratio to completely fill the component.
  - `fit`. Scales the image by aspect ratio to fit the component.

  **Default**: `cover`; **Allowed Values**: `cover`, `fit`
- `hidden` (boolean): A Boolean that indicates whether the component is hidden.

  **Default**: `false`
- `horizontalAlignment` (string) *(deprecated)*: A string that sets the horizontal alignment of the image fill within its component.

  Valid values:

  - `left`. Aligns the left edge of the fill with the left edge of the component.
  - `center` (default). Aligns the horizontal center of the fill with the center of the component.
  - `right`. Aligns the right edge of the fill with the right edge of the component.

  You can use `fillMode` with `horizontalAlignment` to achieve the effect you want. For example, set `fillMode` to `fit` and `horizontalAlignment` to `left` to fit the image based on its aspect ratio and align the left edge of the fill with the left edge of the component. Or set `fillMode` to `cover` and `horizontalAlignment` to right to scale the image horizontally and align the right edge of the fill with the right edge of the component.

  **Default**: `center`; **Allowed Values**: `left`, `center`, `right`
- `identifier` (string): A unique identifier for this component. If you use identifier, it must be unique across the entire document. Apple News requires an identifier if you want to anchor other components to this component. See [`Anchor`](./anchor.md).
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that’s defined at the top level of the document.

  If you don’t define `layout`, Apple News bases size and position on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that’s defined at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`
- `URL` (uri) *(deprecated)*: The URL of an image file.

  If omitted, the thumbnail of the article referenced in the [`ArticleLink`](./articlelink.md) component is used. Images should be high-resolution so they can be smoothly scaled down.

  Image URLs can begin with http://, https://, or bundle://. If the image URL begins with bundle://, the image file must be in the same directory as the document.

  Image filenames should be properly encoded as URLs.

  See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `verticalAlignment` (string) *(deprecated)*: A string that defines the vertical alignment of the article thumbnail within the component.

  **Default**: `center`; **Allowed Values**: `top`, `center`, `bottom`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Article Structure
- [Nesting Components in an Article](../AppleNews/nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Adding a Scene to a Chapter or a Section Header](../AppleNews/adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
- [Creating an Article Link](../AppleNews/creating-an-article-link.md)
  Link to an article by using the article-linking container component.
- [Displaying Components Side By Side](../AppleNews/displaying-components-side-by-side.md)
  Configure a side-by-side, horizontal arrangement of components for your article.
- [object Header](./header.md)
  The component for defining the top area of an article, chapter, or section.
- [object Container](./container.md)
  Properties shared by all container types.
- [object Section](./section.md)
  The component for organizing an article into sections.
- [object Chapter](./chapter.md)
  The component for organizing an article into chapters.
- [object Aside](./aside.md)
  The component for setting apart content that is not directly related to the article, such as promotional content.
- [object CollectionDisplay](./collectiondisplay.md)
  An object used in any container component type to define how the collection of child components is presented.
- [object HorizontalStackDisplay](./horizontalstackdisplay.md)
  The object for displaying components side by side in a Container component.
- [object FlexibleSpacer](./flexiblespacer.md)
  The component for redistributing empty space inside a horizontal stack collection.
- [object Divider](./divider.md)
  The component for defining a horizontal line to visually divide parts of your article.
- [object ArticleLink](./articlelink.md)
  The container component for creating a link to an article.
- [type SupportedArticleIdentifier](./supportedarticleidentifier.md)
  The patterns supported for article identifiers in UUID format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/articlethumbnail)*
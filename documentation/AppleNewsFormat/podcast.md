# Podcast

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding a Podcast show or episode.

**Availability**:
- Apple News Format 1.14+

## Declaration

```
object Podcast
```

## Discussion

Use the `Podcast` component to embed information about a podcast and link to it. You can embed information about a podcast show or episode into an article, and link to that show or episode.

The `Podcast` component uses two optional properties to provide basic layout and color theme customizations:

- `orientation`. By default, the `Podcast` component automatically adjusts the layout of the subcomponents depending on the viewport width of the device. On viewports less than 600 points (iPhone), the layout is vertical with artwork stacked on top of the podcast information. On viewports greater than 600 points (iPad), the layout is horizontal with artwork and podcast information appearing side by side. The artwork is on the left and the podcast information is on the right. If you’d like to specify a horizontal layout regardless of the viewport width of the device, use the `horizontal` property.
- `theme`. By default, the `Podcast` component automatically changes color styles depending on whether Dark Mode is turned on or off for the device the article appears on. If you’d like to specify a light or a dark appearance independent of the device setting, use the `theme` property.

### Example

```json
{
  "components": [
    {
      "role": "podcast",
      "URL": "https://podcasts.apple.com/us/podcast/apple-events/id1473854035" 
    },
    {
      "role": "podcast",
      "URL": "https://podcasts.apple.com/us/podcast/apple-events/id1473854035?i=1000479125753"
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `podcast` for this component.

  **Allowed Values**: `podcast`
- `URL` (uri) *(required)*: The URL of the podcast show or episode you want to embed. The show or episode must be available on Apple Podcasts. Note that a user cannot play the show or episode directly in the article. For more information, see [Apple Podcasts](https://itunespartner.apple.com/podcasts/articles/).

  The URL determines whether it is a show or an episode.

  The following is an example of a podcast show link:

  `https://podcasts.apple.com/us/podcast/apple-events/id1473854035`

  The following is an example of a podcast episode link:

  `https://podcasts.apple.com/us/podcast/apple-events/id1473854035?i=1000479125753`
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You need an `identifie`r for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If you don’t define `layout`, size and position are based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `orientation` (string): The viewport layout of the component.

  Valid values:

  - `horizontal`. Creates a horizontal layout regardless of the viewport width. On screens with viewport width less than 600 points, the artwork and podcast information appear side by side, and the Listen on Apple Podcasts button appears at the bottom. On screens with viewport width greater than 600 points, the Listen on Apple Podcasts button appears below the podcast information.
  - `automatic` (default).  Automatically switches orientation from `vertical` to `horizontal` when the viewport width is 600 points or greater.

  **Default**: `automatic`; **Allowed Values**: `horizontal`, `automatic`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`
- `theme` (string): The color theme of the component.

  Valid Values:

  - `light`. Displays light theme regardless of the device’s color mode.
  - `dark`. Displays dark theme regardless of the device’s color mode.
  - `automatic` (default). Switches automatically from `light` to `dark` when the user turns on Dark Mode.

  **Default**: `automatic`; **Allowed Values**: `light`, `dark`, `automatic`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Audio and Video
- [object Audio](./audio.md)
  The component for adding a playable audio clip.
- [object Music](./music.md)
  The component for adding a playable music file.
- [object Video](./video.md)
  The component for adding a video.
- [object EmbedWebVideo](./embedwebvideo.md)
  The component for adding a web video from Dailymotion, Vimeo, or YouTube.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/podcast)*
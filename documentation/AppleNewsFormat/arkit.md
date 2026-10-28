# ARKit

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding an augmented reality (AR) experience to your article.

**Availability**:
- Apple News Format 1.8+

## Declaration

```
object ARKit
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

## Discussion

Augmented reality (AR) creates user experiences that add 2D or 3D elements to the live view from a device’s camera in a way that makes those elements appear to inhabit the real world. ARKit combines device motion tracking, camera scene capture, advanced scene processing, and display conveniences to simplify the task of building an AR experience. See [`ARKit`](./arkit.md).

Displaying ARKit content in Apple News requires an iOS or iPadOS device with an A9 or later processor.

> ❗ **Important**:  The ARKit feature can’t be previewed on iOS versions earlier than iOS 12. If you are using News Preview, ensure you have Xcode 9 or later installed.

### Example

```json
{
  "components": [
    {
      "role": "arkit",
      "caption": "Lunar Lander",
      "URL": "https://example.com/assets/lunar-lander/main.usdz"
    }
  ]
}
```

## Properties

- `caption` (string) *(required)*: A string that describes the contents of the ARKit stage. The text is  used for VoiceOver. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility.
- `role` (string) *(required)*: Always `arkit` for this component.

  **Allowed Values**: `arkit`
- `URL` (uri) *(required)*: A valid URL to a Universal Scene Description file (USD) file with extension .`usdz`, beginning with `http://`, `https://` or `bundle://`.
- `accessibilityCaption` (string): A caption that describes the augmented reality experience. The text is used for VoiceOver. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines [`Behavior`](./behavior.md) for a component, like [`Parallax`](./parallax.md) or [Springy](https://developer.apple.com/library/archive/documentation/General/Conceptual/Apple_News_Format_Ref/SpringyBehavior.html#//apple_ref/doc/uid/TP40015408-CH73).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `explicitContent` (boolean): This property indicates that the component may contain explicit or graphic content.
- `hidden` (boolean): A boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You need an identifier for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define `layout`, size and position are based on various factors, such as the device type, the length of the content, and the role of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/arkit)*
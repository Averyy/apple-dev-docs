---
url: "https://docs.swift.org/latest/documentation/docc/image"
framework: "Swift-Org/docc"
---

# Image

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

Displays an image in a tutorial.

**Availability**:
- Swift-DocC 5.5+

## Declaration

```swift
@Image(source: ResourceReference, alt: String?) {
    ...
}
```

## Mentions

- [Building an Interactive Tutorial](./building-an-interactive-tutorial.md)

#### Overview

The `Image` directive displays an image in your tutorial. Provide the name of an image and alternative text that describes the image in sufficient detail so screen readers can read that text aloud for people who are blind or have low-vision.

```markdown
@Image(source: overview-hero, alt: "An illustration of a sleeping sloth, hanging from a tree branch.”)
```

Images can exist anywhere in your documentation catalog (’.docc’ directory). but it’s good practice to use subdirectories to organize the content and assets in your documentation. Regardless of organization within your catalog, each image needs to have a unique name.

The supported image file extensions are `png`, `jpg`, `jpeg`, `svg` and `gif`.

> 💡 **Tip**: To differentiate tutorial images from reference documentation images, you may wish to prefix image file names with “tutorial”.

##### Provide Image Variants

To ensure that images render well on both standard and high-resolution displays, and in light and dark appearance modes, you can provide appearance and display scale-aware versions of each image by including specific components in the image filename.

![An image of a filename that’s split into four labeled sections to highlight the individual components. From left to right, the components are the image name, the appearance mode, the display scale, and the file extension.](https://docs.swift.org/latest/images/org.swift.docc/docc-image-filename@2x.png)

For example, the following are all valid DocC image filenames:

- **`sloth.png`**: An image that’s independent of all appearance modes and display scales.
- **`sloth~dark.png`**: An image that’s specific to dark mode, but is display-scale independent.
- **`sloth~dark@2x.png`**: An image that’s specific to dark mode and the 2× display scale.

Omit the appearance and display scale components when specifying an image name for the `source` parameter. For example, if you write `@Image(source: overview-hero, alt: " ... ")` and the reader views that tutorial page **on a display that has dark appearance mode** enabled, the system displays *overview-hero~dark@2x.png*.

At minimum, strive to provide high resolution variants **in light and dark appearance modes.** If you don’t provide a variant that matches the readers context, the system displays the closest matching image variant.

##### Containing Elements

The following tutorial elements can include images.

- [`Chapter`](./chapter.md)
- [`Choice`](./choice.md)
- [`ContentAndMedia`](./contentandmedia.md)
- [`Intro`](./intro.md)
- [`Step`](./step.md)
- [`Tutorial`](./tutorial.md)
- [`Volume`](./volume.md)

## Parameters

- `source`: The name of an image in your documentation catalog (’.docc’ directory). **(required)**

  Omit the appearance (for example `~dark`) and display scale (for example `@2x`) components. The file extension component (for example `.png`) is optional and can be omitted. For more information about the components of an image filename, see [Adding Images to Your Content](./adding-images.md).

  If the image name contains either whitespace characters, commas (`,`), or colons (`:`) you need to surround it with quotation marks (`"`).
- `alt`: Alternative text that describes the image to screen readers. **(required)**


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/image)*
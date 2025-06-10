# mapkit.MarkerAnnotation

**Framework**: MapKit JS  
**Kind**: class

An annotation that displays a balloon-shaped marker at the designated location.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.MarkerAnnotation
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

A  is a balloon-shaped annotation that contains a glyph or text. On the map, the marker appears when its coordinate is in view.

The following example shows a customized marker that specifies a color for the balloon background and the glyph, and provides custom glyph images. Color properties accept either a color name, here “brown” and “green”, or the equivalent hexadecimal color value such as “`#A52A2A`” and “`#008000`”, respectively. Or, you can use a specific color that matches your apps specific design. For more information on standardized colors, see the CSS working group’s list of [`common color names and values`](https://developer.apple.comhttps://drafts.csswg.org/css-color/#named-colors).

```javascript
const portland = new mapkit.Coordinate(45.5231, -122.6765);
const customMarker = new MarkerAnnotation(portland, {
    color: "green",
    glyphColor: "brown",
    glyphImage: { 1: "glyphImage.png" },
    selectedGlyphImage: { 1: "detailedIcon.png", 2: "detailedIcon_2x.png", 3: "detailedIcon_3x.png" }
});
```

The following example shows a marker annotation with a custom callout implemented by the callout delegate. In this example, the annotation is a dot when selected because [`selectedGlyphImage`](mapkit.markerannotation/selectedglyphimage.md) isn’t used.

```javascript
const calloutDelegate = {
    calloutRightAccessoryForAnnotation: function() {
        const accessoryViewRight = document.createElement("a");
        accessoryViewRight.className = "right-accessory-view";
        accessoryViewRight.href = "https://www.nps.gov/stli/index.htm";
        accessoryViewRight.target = "_blank";
        accessoryViewRight.appendChild(document.createTextNode("ⓘ"));

        return accessoryViewRight;
    }
};

const annotation = new mapkit.MarkerAnnotation(new mapkit.Coordinate(40.6892, -74.0445), {
    title: "Title",
    subtitle: "Subtitle",
    callout: calloutDelegate
});
```

## Topics

### Creating a marker annotation
- [mapkit.MarkerAnnotation](mapkit.markerannotation/mapkit.markerannotation.md)
  Creates a marker annotation at the coordinate location with provided options.
- [MarkerAnnotationConstructorOptions](markerannotationconstructoroptions.md)
  An object containing the options that create a marker annotation.
### Setting visibility
- [subtitleVisibility](mapkit.markerannotation/subtitlevisibility.md)
  A value that determines the behavior of the subtitle’s visibility.
- [titleVisibility](mapkit.markerannotation/titlevisibility.md)
  A value that determines the behavior of the title’s visibility.
- [mapkit.FeatureVisibility](mapkit.featurevisibility.md)
  Constants indicating the visibility of different adaptive map features.
### Setting appearance
- [color](mapkit.markerannotation/color.md)
  The background color of the balloon.
- [glyphColor](mapkit.markerannotation/glyphcolor.md)
  The fill color of the glyph.
### Setting the glyph image and text
- [glyphText](mapkit.markerannotation/glyphtext.md)
  The text to display in the marker balloon.
- [glyphImage](mapkit.markerannotation/glyphimage.md)
  The image to display in the marker balloon.
- [selectedGlyphImage](mapkit.markerannotation/selectedglyphimage.md)
  The image to display in the marker balloon when the user selects the marker.

## Relationships

### Inherited By
- [mapkit.Annotation](mapkit.annotation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.markerannotation)*
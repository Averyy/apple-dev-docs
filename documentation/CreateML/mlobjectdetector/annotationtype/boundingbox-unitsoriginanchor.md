# MLObjectDetector.AnnotationType.boundingBox(units:origin:anchor:)

**Framework**: Create ML  
**Kind**: case

An annotation type that defines a rectangle around an object within an image.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case boundingBox(units: MLBoundingBoxUnits = .pixel, origin: MLBoundingBoxCoordinatesOrigin = .topLeft, anchor: MLBoundingBoxAnchor = .center)
```

#### Discussion

To use bounding box annotations, you must tell Create ML how to interpret your annotations.

- Use [`MLBoundingBoxUnits`](mlboundingboxunits.md) to specify the coordinate units of your bounding boxes. - Use [`MLBoundingBoxAnchor`](mlboundingboxanchor.md) to specify the location in the bounding box its coordinates refer to. - Use [`MLBoundingBoxCoordinatesOrigin`](mlboundingboxcoordinatesorigin.md) to specify the part of the image the annotations use as their origin.

#### Formatting a Bounding Box Json Annotation File

The base of the JSON file must contain an array of the following JSON object structure.

| Name | Type | Value |
| --- | --- | --- |
| `imagefilename` | String | The name of the image’s file. |
| `annotation` | Array | An array of annotation JSON objects. |

Each JSON object in the `annotation` array must have the following JSON object structure.

| Name | Type | Value |
| --- | --- | --- |
| `label` | String | The name of the annotated object. |
| `coordinates` | JSON object | The location of the object and the area it occupies in the image. |

The `coordinate` JSON object must have the following structure. The origin of the image is the upper-left corner. The `x`-values increase from left to right, and the `y`-values increase from the top to the bottom.

| Name | Type | Value |
| --- | --- | --- |
| `x` | Number | The `x`-coordinate of the annotation’s origin, which `MLBoundingBoxCoordinatesOrigin` defines. |
| `y` | Number | The `y`-coordinate of the annotation’s origin, which `MLBoundingBoxCoordinatesOrigin` defines. |
| `width` | Number | The width of the annotation’s bounding box. |
| `height` | Number | The height of the annotation’s bounding box. |

As an example, the following JSON file has correct structure with one image file (`"cat and dog.png"`) in its base array, which has two annotations.

```None
// JSON file
  [{
    "imagefilename": "cat and dog.png",
    "annotation":
    [
      {
        "label": "cat",
        "coordinates":
        {
          "y": 2.0,
          "x": 3.9,
          "height": 40.1,
          "width": 20.0
        }
      }, {
        "label": "dog",
        "coordinates":
        {
          "y": 40.0,
          "x": 38.9,
          "height": 100.1,
          "width": 70.0
        }
      }
    ]
  },
  ... ]
```

A typical annotation JSON file has many more objects in its base array, one for each image file.

## See Also

- [enum MLBoundingBoxUnits](mlboundingboxunits.md)
  The units a bounding box annotation uses to define its position and size.
- [enum MLBoundingBoxAnchor](mlboundingboxanchor.md)
  A location within a bounding box that an annotation’s coordinates use as their reference point.
- [enum MLBoundingBoxCoordinatesOrigin](mlboundingboxcoordinatesorigin.md)
  The location within an image that an annotation’s coordinates use as their origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:))*
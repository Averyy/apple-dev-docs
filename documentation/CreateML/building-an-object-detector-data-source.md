# Building an object detector data source

**Framework**: Create ML

Arrange your training data for an object detector in one of several different structured ways.

#### Overview

The general tasks for structuring data for training an object detector are the following:

- Collect a set of images with sufficient size and diversity to reflect the data set you expect to predict on.
- Create annotations for each image, containing labels and bounding boxes for each labeled object.
- Structure these in a folder with an annotation file or `DataFrame` to best suit your use case.

Create ML accepts several data-source types for an object detector. Two major kinds of data are inherent in any labeled data set:

These kinds of data represent the two steps required to build an annotated data set to train an object detector model. First, collect the images you wish to train on. Second, annotate them with labeled bounding boxes that show the location of the objects you want your model to recognize. Both of these steps, as well as how to combine this data into a data source, are detailed below.

For more information about the object detector data-source types the Create ML API supports, see [`MLObjectDetector`](mlobjectdetector.md).

##### Collect Images

Before you train, ensure that the training set has sufficient sample size and diversity within each label. Make your data reflect what your model sees in practice.

The images can be any standard image format. After you collect your training set, put it in a common folder, and proceed with annotations.

##### Format a Bounding Box Json Annotation

Annotating images in an object detector teaches your model what objects it’s trying to recognize. Define zero, one, or multiple bounding boxes within each image in your training data set that show where an object is and what kind of object it is.

Here is a training data image:

![A picture of a croissant on a breakfast table.](https://docs-assets.developer.apple.com/published/46c42d0543a634784b3727dde375217a/building-an-object-detector-data-source-4%402x.png)

Here is an illustration of how a bounding box on a training data image is structured:

![A picture of a waffle on a breakfast table. This particular annotation has the origin in the top left.](https://docs-assets.developer.apple.com/published/9e554515229714e84c8f9efdfce9d309/building-an-object-detector-data-source-5%402x.png)

One way to structure your annotations is with a JSON annotation file, structured like this:

| Name | Type | Value |
| --- | --- | --- |
| `imagefilename` | String | The name of the image’s file. |
| `annotation` | Array | An array of annotation JSON objects. |

Each JSON object in the `annotation` array must have the following JSON object structure.

| Name | Type | Value |
| --- | --- | --- |
| `label` | String | The name of the annotated object. |
| `coordinates` | JSON object | The location of the object and the area it occupies in the image. |

The `coordinates` JSON object must have the following structure.

| Name | Type | Value |
| --- | --- | --- |
| `x` | Number | The `x`-coordinate of the annotation’s anchor location with respect to the image origin, which `MLBoundingBoxCoordinatesOrigin` defines. |
| `y` | Number | The `y`-coordinate of the annotation’s anchor location with respect to the image origin, which `MLBoundingBoxCoordinatesOrigin` defines. |
| `width` | Number | The width of the annotation’s bounding box. |
| `height` | Number | The height of the annotation’s bounding box. |

When put together, a full object detector annotation file looks like the following:

```None
[
{
  "imagefilename": "breakfast_0.png",
  "annotation": [
    {
      "coordinates": {
        "y": 156.062,
        "x": 195.122,
        "height": 148.872,
        "width": 148.03
      },
      "label": "Waffle"
    }
  ]
},
{
  "imagefilename": "breakfast_1.png",
  "annotation": [
    {
      "coordinates": {
        "y": 98.9209,
        "x": 128.744,
        "height": 151.798,
        "width": 153.056
      },
      "label": "Waffle"
    },
    {
      "coordinates": {
        "y": 182.254,
        "x": 256.172,
        "height": 159.712,
        "width": 208.147
      },
      "label": "Croissant"
    }
  ]
},
{
  "imagefilename": "breakfast_2.png",
  "annotation": [
    {
      "coordinates": {
        "y": 116.875,
        "x": 354.375,
        "height": 98.7501,
        "width": 85
      },
      "label": "Croissant"
    }
  ]
},
{
  "imagefilename": "breakfast_3.png",
  "annotation": [
    {
      "coordinates": {
        "y": 149.75,
        "x": 182.114,
        "height": 76.3134,
        "width": 101.063
      },
      "label": "Croissant"
    }
  ]
}
]
```

##### Customize Annotations

Each element of the annotated JSON references one image with `imagefilename` and defines one array of annotations in `annotation`. Make sure to include the file extension in the filename. You can define any number of labeled objects within a single image. Each element of the array contains `coordinates`, consisting of the `x`-coordinate, `y`-coordinate, `width`, and `height` of the bounding box.

You can define the origin from which x- and y-coordinates are specified as either `bottom left` or `top left` by using `MLBoundingBoxCoordinatesOrigin`, with `top left` as a default value.

Additionally, you can define an `MLBoundingBoxAnchor` with possible values of `center`, `top left`, and `bottom left`, with `center` as a default value. The anchor shows the position of the bounding box relative to the origin, so if you select `center`, then the x- and y-values in the annotation point to the center of each bounding box.

Finally, you can define `MLBoundingBoxUnits` as either `pixels` or `normalized`. The default option is `pixels`, which counts integer numbers of pixels from the origin. In contrast, `normalized` is on a scale from 0.0 to 1.0 in both the x- and y-dimensions.

If `MLBoundingBoxUnits` is set to `normalized`, then the annotation might look like the following:

```None
"annotation": [
{
  "coordinates": {
    "y": 0.13,
    "x": 0.16,
    "height": 0.12,
    "width": 0.12
  },
  "label": "Waffle"
}
]
```

Here is the full `boundingBox` case defined in code:

```None
/// A typical annotation JSON file has many more objects in its base
/// array, one for each image file.
case boundingBox(units: MLBoundingBoxUnits = .pixel, origin: MLBoundingBoxCoordinatesOrigin = .topLeft, anchor: MLBoundingBoxAnchor = .center)
```

For more detail, see [`MLObjectDetector.AnnotationType`](mlobjectdetector/annotationtype.md).

##### Build a Data Source From Images and Annotations

The simplest way to structure your data is using the `directoryWithImagesAndJsonAnnotation` case. Take the collected images and exactly one JSON annotation file, and put them all in a single folder.

![Flow diagram of an annotated images data-source file arrangement. The parent folder contains images and one annotation file.](https://docs-assets.developer.apple.com/published/a327e0401c9603058611ad3668f318e6/building-an-object-detector-data-source-1%402x.png)

Use this folder to train an object detector. The Create ML App uses this case, and you can drag a folder into a training well to train an object detector.

![Screenshot of Create ML App showing a folder dragged into the training well for Object Detection.](https://docs-assets.developer.apple.com/published/00aae46d22966c3c16840b9f7da115ac/building-an-object-detector-data-source-7%402x.png)

After you train a model in the Create ML app, you can generate bounding boxes from the trained model in the Preview tab.

##### Build a Data Source From a Directory with Images

The `DataSource` case `directoryWithImages` is similar to `directoryWithImagesAndJsonAnnotation`, except you don’t need to nest the JSON annotation file in the folder with the images. Instead, you call it by reference from any specified URL.

![Flow diagram of an annotated images data-source file arrangement. The parent folder contains images with one annotation file separately.](https://docs-assets.developer.apple.com/published/38848ccaa70c2284484c7a3a78487979/building-an-object-detector-data-source-2%402x.png)

##### Build a Data Source From a Data Frame

In the case `frame`, you call an object detector from a single `DataFrame`. Rather than store your data in a directory structure, the format of this table is similar to the annotation file, where the `DataFrame` has the following columns:

- `imageColumn`: contains image file locations
- `annotationColumn`: contains the annotations for that particular image, using the same JSON structure defined above.

![Overview of an DataFrame structured for an Object Detector Annotation, with one column with image filenames and a 2nd with annotations.](https://docs-assets.developer.apple.com/published/c4006baa765fa154de69f53f6f51727f/building-an-object-detector-data-source-3%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/building-an-object-detector-data-source)*
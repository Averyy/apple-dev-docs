# new ImageAnnotation(location, options)

**Framework**: MapKit JS  
**Kind**: init

Creates an image annotation with a URL to its image and a coordinate.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(
        location: Coordinate | Place | SearchAutocompleteResult,
        options: ImageAnnotationConstructorOptions,
    );
```

#### Discussion

This example shows two image annotations: one with a minimally defined image, and one with more options filled in:

```javascript
const coordinate = new mapkit.Coordinate(38.897957, -77.036560);

// The house logo is a white square.
// The image size is 32 x 32. Becuase the default anchor point is the bottom center
// of the image, offset the anchor by (0, -16) to make the center of the
// image the anchor point.
const houseOptions = {
    title: "The White House",
    subtitle: "1600 Pennsylvania Ave NW",
    url: { 1: "/images/house.png", 2: "/images/house_2x.png"},
    anchorOffset: new DOMPoint(0, -16)
};
const houseAnnotation = new mapkit.ImageAnnotation(coordinate, houseOptions);
map.addAnnotation(houseAnnotation);

// This is how to implement a red pin.
const pinOptions = {
    url: {
        1: "/images/pin-red.png",
        2: "/images/pin-red_2x.png"
    }
};
const pinAnnotation = new mapkit.ImageAnnotation(coordinate, pinOptions);
map.addAnnotation(pinAnnotation);
```

## Parameters

- `location`: The coordinate where this annotation appears.
- `options`: A hash of properties that initialize the annotation. The   hash needs to include  . MapKit JS displays an optional   and   in a callout if they’re present.

## See Also

- [interface ImageAnnotationConstructorOptions](imageannotationconstructoroptions.md)
  An object containing options for creating an image annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imageannotation/imageannotationconstructor)*
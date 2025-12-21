# AnnotationCalloutDelegate

**Framework**: MapKit JS  
**Kind**: struct

Methods for customizing the behavior and appearance of an annotation callout.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface AnnotationCalloutDelegate
```

#### Overview

You can customize an annotation callout by replacing the callout element, or by providing custom content to display inside a standard callout bubble. The callout delegate contains methods you implement to customize the appearance and behavior of the callout. All the methods are optional, enabling you to override any or all of the behavior.

##### Creating a Custom Callout

This example shows how to replace the standard callout with a custom callout for a [`MarkerAnnotation`](markerannotation.md).

```javascript
const calloutDelegate = {

    // Return a div element and populate it with information from the
    // annotation, including a link to a review site.
    calloutElementForAnnotation: function(annotation) {
        const element = document.createElement("div");
        element.className = "review-callout";
        const title = element.appendChild(document.createElement("h1"));
        title.textContent = annotation.title;
        const link = element.appendChild(document.createElement("a"));
        link.href = annotation.data.reviewLink;
        link.textContent = "Review";
        // Add more content.
        element.style.width = "240px";
        element.style.height = "100px";
        return element;
    },
};

// Create an annotation with a link to be displayed in the callout.
const annotation = new mapkit.MarkerAnnotation(
    new mapkit.Coordinate(35.7019272, 139.575628),
    {
        callout: calloutDelegate,
        title: "...",
        data: {
            reviewLink: "http://..."    // Link to review site.
            // More info like address, phone number, etc.
        }
    }
);
```

##### Customizing the Content in a Standard Callout

You may want to provide your own content to display inside the callout bubble, without replacing the whole element as in the previous code listing. The following example is similar to the previous one, but uses the standard callout bubble to display custom content.

```javascript
const calloutDelegate = {
    // Return a div element and populate it with information from the
    // annotation, including a link to a review site.
    calloutContentForAnnotation: function(annotation) {
        const element = document.createElement("div");
        element.className = "review-callout-content";
        const title = element.appendChild(document.createElement("h1"));
        title.textContent = annotation.title;
        const link = element.appendChild(document.createElement("a"));
        link.href = annotation.data.reviewLink;
        link.textContent = "Review";
        // Add more content.
        return element;
    }
};

// Create an annotation with a link to be displayed in the callout.
const annotation = new mapkit.MarkerAnnotation(
    new mapkit.Coordinate(35.7019272, 139.575628),
    {
        callout: calloutDelegate,
        title: "...",
        data: {
            reviewLink: "http://..."    // Link to review site.
            // More info like address, phone number, etc.
        }
    }
);
```

## Topics

### Customizing callout appearance
- [calloutAnchorOffsetForAnnotation(annotation, size)](annotationcalloutdelegate/calloutanchoroffsetforannotation.md)
  Returns a point determining the callout’s anchor offset.
- [calloutShouldAppearForAnnotation(annotation)](annotationcalloutdelegate/calloutshouldappearforannotation.md)
  Determines whether the callout appears for an annotation.
- [calloutShouldAnimateForAnnotation(annotation)](annotationcalloutdelegate/calloutshouldanimateforannotation.md)
  Determines whether the callout animates.
- [calloutAppearanceAnimationForAnnotation(annotation)](annotationcalloutdelegate/calloutappearanceanimationforannotation.md)
  Returns a CSS animation to use when the callout appears.
### Providing elements
- [calloutContentForAnnotation(annotation)](annotationcalloutdelegate/calloutcontentforannotation.md)
  Returns custom content for the callout bubble.
- [calloutElementForAnnotation(annotation)](annotationcalloutdelegate/calloutelementforannotation.md)
  Returns an element representing a custom callout.
- [calloutLeftAccessoryForAnnotation(annotation)](annotationcalloutdelegate/calloutleftaccessoryforannotation.md)
  Returns an element to use as a custom accessory on the left side of the callout content area.
- [calloutRightAccessoryForAnnotation(annotation)](annotationcalloutdelegate/calloutrightaccessoryforannotation.md)
  Returns an element to use as a custom accessory on the right side of the callout content area.

## See Also

- [const CollisionMode](collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
- [const DisplayPriority](displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [interface Size](size.md)
  A structure that represents a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationcalloutdelegate)*
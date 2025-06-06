# init(location:title:subtitle:summary:detailTitle:detailSubtitle:detailSummary:pinImage:)

**Framework**: CarPlay  
**Kind**: init

Creates a point of interest for a specific location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
convenience init(location: MKMapItem, title: String, subtitle: String?, summary: String?, detailTitle: String?, detailSubtitle: String?, detailSummary: String?, pinImage: UIImage?)
```

#### Discussion

[`CPPointOfInterestTemplate`](cppointofinteresttemplate.md) displays selectable instances of `CPPointOfInterest` as annotations on the template’s map, and as items in a scrollable picker that the template overlays on the map. When the user selects a point of interest, the template displays a detail card that contains secondary information and optional actions the user can perform.

If you use a custom `pinImage`, provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property.

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## Parameters

- `location`: The map item that contains the point of interest’s geographical information.
- `title`: The title that the picker displays for the item.
- `subtitle`: The subtitle that the picker displays for the item.
- `summary`: A brief summary that the picker displays for the item.
- `detailTitle`: The detail card’s title.
- `detailSubtitle`: The detail card’s subtitle.
- `detailSummary`: A brief summary that the detail card displays.
- `pinImage`: A custom image that the map annotation displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/init(location:title:subtitle:summary:detailtitle:detailsubtitle:detailsummary:pinimage:))*
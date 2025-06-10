# mapkit.LookAroundPreview

**Framework**: MapKit JS  
**Kind**: class

A class that renders a preview of a LookAround view.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
interface mapkit.LookAroundPreview
```

## Mentions

- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)
- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

> **Note**:  The full bundle of MapKit JS doesn’t implement this class.

Use a `mapkit.LookAroundPreview` to create preview imagery for a specific geographic location on the map.

> **Note**: Not all places support Look Around.

The following example contains the two elements needed to display a Look Around View on a web page:

![A screenshot showing a map view with a marker showing New York Public Library in New York, NY, and a smaller Look Around preview framing the library on the top left.](https://docs-assets.developer.apple.com/published/e7f9457ee4a834f156cf05cfd1e69252/LookAroundPreview-cl-01%402x.png)

The HTML code below implements a web page that renders a `container` which has both a map and a Look Around preview.

```html
<script
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.core.js"
  crossorigin async
  data-callback="initMapKit"
  data-token="YOUR TOKEN HERE"
  data-libraries="map,annotations,look-around,services"></script>
<style>
#map {
  width: 100%;
  height: 100%;
}
#container {
  position: absolute;
  top: 20px;
  left: 20px;
  border-radius: 20px;
  overflow: hidden;
  width: 200px;
  height: 150px;
}
</style>

<main>
  <div id="map"></div>
  <div id="container"></div>
</main>
```

The JavaScript listing below implements a MapKitJS map object that the web page displays inside the `<div id="map">` element of the page, with a Look Around preview displays inside the `<div id="container">` element. The code centers the map on the area near the New York Public Library in New York City using a PlaceID. The Look Around preview on the map shows a view of The New York Public Library building. For more information on obtaining a PlaceID for a specific location. For more information on Place IDs, see [`Identifying unique locations with Place IDs`](https://developer.apple.comhttps://developer.apple.com/maps/place-id-lookup/).

```javascript
async function initializeMapKitJS() {
  if (!window.mapkit || window.mapkit.loadedLibraries.length === 0) {
    await new Promise(res => window.initMapKit = res)
    delete window.initMapKit
  }
}

(async () => {
  await initializeMapKitJS();
  // Look Around view code

  const placeLookup = new mapkit.PlaceLookup();
  const place = await new Promise(
      resolve => placeLookup.getPlace(
        // The New York Public Library, 42nd St & 5th Ave,New York, NY
        "I88F02FEA4499C61D",
        (error, result) => resolve(result)
      )
  );

  const lookAround = new mapkit.LookAroundPreview(
      document.getElementById("container"),
      place
  );

  const map = new mapkit.Map("map", {
    center: place.coordinate,
    cameraDistance: 7000,
    showsPointsOfInterest: false,
    annotations: [
      new mapkit.PlaceAnnotation(place, {
        selected: true
      })
    ]
  });

})()
```

#### Handling Look Around Loading States

LookAroundPreview object dispatches the following events:

- `load`: The view is loaded.
- `error`: The view has encountered an error, for example, in an unsupported browser, or a location with no look around imagery.
- `readystatechange`: [`readyState`](mapkit.lookaroundpreview/readystate.md) has changed.
- `open-dialog`: The view is about to expand.
- `leave-dialog`: The view is about to contract.

## Topics

### Creating a Look Around preview
- [mapkit.LookAroundPreview](mapkit.lookaroundpreview/mapkit.lookaroundpreview.md)
  Creates a Look Around preview you embed on a webpage and initializes it with the constructor options you choose.
### Controlling the interactions with a Look Around view
- [isNavigationEnabled](mapkit.lookaroundpreview/isnavigationenabled.md)
  A Boolean value that indicates whether someone can navigate inside the Look Around preview.
- [isScrollEnabled](mapkit.lookaroundpreview/isscrollenabled.md)
  A Boolean value that indicates whether someone can scroll the Look Around preview.
- [isZoomEnabled](mapkit.lookaroundpreview/iszoomenabled.md)
  A Boolean value that indicates whether someone can zoom the Look Around preview.
### Controlling additional information the Look Around view displays
- [showsPointsOfInterest](mapkit.lookaroundpreview/showspointsofinterest.md)
  A Boolean value that indicates whether the Look Around preview shows points of interest (POIs).
- [showsRoadLabels](mapkit.lookaroundpreview/showsroadlabels.md)
  A Boolean value that indicates whether the Look Around preview shows road labels.
### Positioning a badge
- [badgePosition](mapkit.lookaroundpreview/badgeposition.md)
  A value you set to specify the position of a badge on the Look Around preview.
- [mapkit.LookAround.BadgePositions](mapkit.lookaround.badgepositions.md)
  Values that control the positions of a badge on a Look Around preview.
### Controlling the LookAround dialog
- [openDialog](mapkit.lookaroundpreview/opendialog.md)
  Creates a new Look Around preview object.
### Getting information about the Look Around object and its state
- [element](mapkit.lookaroundpreview/element.md)
  A property that represents the Look Around preview’s containing DOM element.
- [scene](mapkit.lookaroundpreview/scene.md)
  A property that represents the current location of the view.
- [padding](mapkit.lookaroundpreview/padding.md)
  The values that define content padding within the Look Around preview frame.
- [readyState](mapkit.lookaroundpreview/readystate.md)
  A property that represents the loading state of the Look Around preview object.
- [mapkit.LookAround.ReadyStates](mapkit.lookaround.readystates.md)
  Values that indicate the state of the Look Around object in the browser.
### Closing and releasing a Look Around view
- [destroy](mapkit.lookaroundpreview/destroy.md)
  A method you call to destroy the Look Around preview.

## See Also

- [mapkit.LookAround](mapkit.lookaround.md)
  A view that allows someone to see a street level view of a place.
- [LookAroundOptions](lookaroundoptions.md)
  Options for initializing a LookAround view.
- [LookAroundPreviewOptions](lookaroundpreviewoptions.md)
  Options for initializing a LookAroundPreview object.
- [mapkit.LookAroundScene](mapkit.lookaroundscene.md)
  Object that represents the current location of the view.
- [CommonLookAroundOptions](commonlookaroundoptions.md)
  Options that control the behavior of Look Around views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.lookaroundpreview)*
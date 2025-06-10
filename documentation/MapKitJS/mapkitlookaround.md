# mapkit.LookAround

**Framework**: MapKit JS  
**Kind**: class

A view that allows someone to see a street level view of a place.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
interface mapkit.LookAround
```

## Mentions

- [Loading the latest version of MapKit JS](loading-the-latest-version-of-mapkit-js.md)
- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

> **Note**:  The full bundle of MapKit JS doesn’t implement this class.

Use a Look Around view to create street level imagery for a specific geographic location on the map. You can, optionally, enable someone to navigate inside this view to allow them to explore the place at street level or zoom the view for a larger screen experience.

> **Note**: Not all places support Look Around.

The following example contains the two elements needed to display a Look Around View on a web page:

![A screenshot showing the Look Around view framing Cherry Hill Fountain, with a Point of Interest Marker.](https://docs-assets.developer.apple.com/published/e3ef0f4db9e0eb675c326ad786aad5e3/LookAround-cl-01%402x.png)

The HTML code below implements a web page that renders a `container` which has a label that provides a description of the place the Look Around view displays.

```html
<script
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.core.js"
  crossorigin async
  data-callback="initMapKit"
  data-token="YOUR TOKEN HERE"
  data-libraries="look-around,services"></script>
<style>
#container { width: 735px; height: 552px }
</style>

<div id="container"></div>
```

The JavaScript listing below implements a MapKitJS Look Around object that the web page displays inside the `<div id="container">` element of the page. The Look Around view shows a navigable view of Cherry Hill Fountain in Central Park in New York City that Look Around renders using a PlaceID. For more information on obtaining a PlaceID for a specific location. For more information on Place IDs, see [`Identifying unique locations with Place IDs`](https://developer.apple.comhttps://developer.apple.com/maps/place-id-lookup/).

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
          // The PlaceID that represents Cherry Hill Fountain, Central Park, New York, NY
          "IEA18943388D2216C",
          (error, result) => resolve(result)
      )
  );

  // Create an interactive look around view.
  const lookAround = new mapkit.LookAround(
      document.getElementById("container"),
      place,
      {
          // Allow users to expand the view.
          showsDialogControl: true
      }
  );

})()
```

#### Handling Look Around Loading States

Look Around view dispatches the following events:

- `load`: Look Around view is loaded.
- `error`: Look Around view has encountered an error, for example, in an unsupported browser, or a location with no look around imagery.
- `readystatechange`: [`readyState`](mapkit.lookaround/readystate.md) has changed.
- `open-dialog`: Look Around view is about to expand.
- `leave-dialog`: Look Around view is about to contract.
- `close`: The user has interacted with the close control.

## Topics

### Creating a Look Around view
- [mapkit.LookAround](mapkit.lookaround/mapkit.lookaround.md)
  Creates a Look Around object you embed on a webpage and initializes it with the constructor options you choose.
### Controlling the interactions with a Look Around view
- [isNavigationEnabled](mapkit.lookaround/isnavigationenabled.md)
  A Boolean value that indicates whether someone can navigate inside the Look Around view.
- [isScrollEnabled](mapkit.lookaround/isscrollenabled.md)
  A Boolean value that indicates whether someone can scroll the Look Around view.
- [isZoomEnabled](mapkit.lookaround/iszoomenabled.md)
  A Boolean value that indicates whether someone can zoom the Look Around view.
### Controlling additional information the Look Around view displays
- [showsPointsOfInterest](mapkit.lookaround/showspointsofinterest.md)
  A Boolean value that indicates whether the Look Around view shows points of interest (POIs).
- [showsRoadLabels](mapkit.lookaround/showsroadlabels.md)
  A Boolean value that indicates whether the Look Around view shows road labels.
### Controlling the Look Around dialog
- [openDialog](mapkit.lookaround/opendialog.md)
  A Boolean value that indicates whether to expand the Look Around view.
### Controlling the display of window controls
- [showsCloseControl](mapkit.lookaround/showsclosecontrol.md)
  A Boolean value that indicates whether the Look Around view displays a close control.
- [showsDialogControl](mapkit.lookaround/showsdialogcontrol.md)
  A Boolean value that indicates whether the Look Around view displays shows a control that allow someone to expand the Look Around view.
### Getting information about the Look Around object and its state
- [element](mapkit.lookaround/element.md)
  A property that represents the Look Around view’s containing DOM element.
- [scene](mapkit.lookaround/scene.md)
  A property that represents the current location of the view.
- [padding](mapkit.lookaround/padding.md)
  The values that define content padding within the Look Around view’s frame.
- [readyState](mapkit.lookaround/readystate.md)
  A value that represents the loading state of the Look Around object.
- [mapkit.LookAround.ReadyStates](mapkit.lookaround.readystates.md)
  Values that indicate the state of the Look Around object in the browser.
### Closing and releasing a Look Around view
- [destroy](mapkit.lookaround/destroy.md)
  A method you call to destroy the Look Around view.

## See Also

- [LookAroundOptions](lookaroundoptions.md)
  Options for initializing a LookAround view.
- [mapkit.LookAroundPreview](mapkit.lookaroundpreview.md)
  A class that renders a preview of a LookAround view.
- [LookAroundPreviewOptions](lookaroundpreviewoptions.md)
  Options for initializing a LookAroundPreview object.
- [mapkit.LookAroundScene](mapkit.lookaroundscene.md)
  Object that represents the current location of the view.
- [CommonLookAroundOptions](commonlookaroundoptions.md)
  Options that control the behavior of Look Around views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.lookaround)*
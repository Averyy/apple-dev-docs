# MapKit JS 5

**Framework**: MapKit JS

Use the most up-to-date version of MapKit JS on your website.

#### Overview

This document includes release notes for updates to MapKit JS 5. You can learn more about MapKit JS version numbers and how to automatically link to the latest available version in [`Loading the latest version of MapKit JS`](loading-the-latest-version-of-mapkit-js.md).

##### 580

###### New Features

- MapKit JS now supports TypeScript definitions as part of the DefinitelyTyped project; see the `@types/apple-mapkit` package.
- Introduced a loader to make integrating MapKit JS into projects more convenient.

##### 579

###### New Features

- [`TransportType`](transporttype.md) supports a new transport type, [`Cycling`](transporttype/cycling.md), for directions and ETAs.
- Introduced the ability to enable 360-degree interactive Look Around imagery with [`LookAround`](lookaround.md) and [`LookAroundPreview`](lookaroundpreview.md).

###### Updates

- The map view and Look Around view respond to user font size preferences, and Dynamic Types on iOS. (Feedback ID: 12784220)
- The map view now pans or zooms in response to the mouse wheel and track pad scrolls. (Feedback ID: 12019011)
- Updated Marker annotation styles.

##### 578112

###### New Features

- The framework now supports expanded point-of-interest categories.

##### 578279

###### Updates

- Updated maps link format.

##### 57853

###### New Features

- Improved cartography styling.
- New label styles for physical feature like mountain ranges.

##### 5781

###### New Features

- Introduced a new way to generate developer tokens.
- Introduced [`PlaceSelectionAccessory`](placeselectionaccessory.md) and [`PlaceDetail`](placedetail.md), which allow developers to display details of a location.
- Introduced [`PlaceAnnotation`](placeannotation.md), which  allows developers to place markers with iconography from the map view.
- Introduced Place ID and its lookup API.
- Introduced new Search filtering capabilities to enforce strict search region, or only return address locations.

##### 5776

###### New Features

- Content Security Policy is now supported.

##### 57699

###### Updates

- Prevent erroneous source map loading errors in Web Inspector (Feedback ID: 4632607)

##### 5767

###### New Features

- Improved map control sizing.

##### 57567

###### Updates

- Fixed a Null is not an object error (Feedback ID: 4342930)

##### 57552

###### New Features

- Physical features on the map view are now selectable.

##### 5754

###### New Features

- Introduced a new way to load MapKit JS, with smaller payloads, optional libraries, and quicker initialization.

##### 5741

###### New Features

- Map features (point-of-interest and territory labels) are now selectable.

##### 5731

###### New Features

- Introduced an option to hint preferred load priority of the map view.

##### 57253

###### New Features

- Relaxed minimal zoom to make the entire world visible when the map view is wider than 1024 pixels.

###### Updates

- Ended support for Internet Explorer 11 and legacy Microsoft Edge.

##### 5722

###### New Features

- Routing request can now be made with “avoid tolls.”

##### 5630

###### New Features

- Modernized map view look and feel.

##### 5560

###### Updates

- Corrected annotation alignment after browser zoom in Safari (Feedback ID: 7469504)

##### 5550

###### New Features

- Return origin/destination information in Directions and ETAs response (Feedback ID: 8669255)

###### Updates

- Fixed an issue causing setting padding doesn’t respect rotation on creating new map (Feedback ID: 3565752)

##### 5520

###### Updates

- Fixed an issue that causes setting [`cameraBoundary`](map/cameraboundary.md) to change the map region. (Feedback ID: 3518887)

##### 5502

###### New Features

- Introduced new styles for built-in controls (zoom buttons, map type picker, etc).
- Introduced a new map type popover.
- Introduced a new user location annotation style.
- Introduced a new [`None`](collisionmode/none.md) collision mode for annotations.

##### 5490

###### Updates

- Fixed an issue causing [`anchorOffset`](annotationconstructoroptions/anchoroffset.md) to be disregarded (Feedback ID: 7789168)

##### 5460

###### New Features

- Calling `Event.preventDefault()` on `single-tap` event now prevents annotation selection.

##### 5450

MapKit JS 5.45.0 introduces new APIs for overlay styling and animation and a new API for searching Points of Interest within a region, and includes bug fixes.

###### New Features

- Added the ability to draw polyline overlays dynamically with new primitives for polyline overlay animation. The start and end point of the polyline rendering can be programmatically controlled with [`strokeStart`](style/strokestart.md) and [`strokeEnd`](style/strokeend.md) properties.
- Introduced the [`LineGradient`](linegradient.md) class for specifying color gradients on polyline overlays.
- Added the ability to search Points of Interest in a specific region with the new [`PointsOfInterestSearch`](pointsofinterestsearch.md) API.

###### Updates

- Updated the [`addItems(items)`](map/additems.md) method to return the items passed.

##### 5440

MapKit JS 5.44.0 introduces new properties for Directions, increases the maximum zoom level for Standard maps, and includes a bug fix for mouse event handling.

###### New Features

- Added [`departureDate`](directionsrequest/departuredate.md) and [`arrivalDate`](directionsrequest/arrivaldate.md) properties to the [`Directions`](directions.md) API that enable more accurate travel time predictions based on arrival or departure date.
- Increased the maximum zoom level on the Standard style map to improve visibility of indoor map details.

###### Updates

- Updated the behavior for disabled overlays so that they no longer capture `single-tap` events. For more information see [`Handling map events`](handling-map-events.md).

##### 5431

MapKit JS 5.43.1 includes a bug fix for setting the visible region on map construction.

###### Updates

- Ensured the specified visible region is honored on map construction. (Feedback ID: 7626496)

##### 5421

MapKit JS 5.42.1 includes bug fixes for rotation events and map regions.

###### Updates

- Ensured that `preventDefault()` can be used with `rotation-start`,  like other map events described in [`Handling map events`](handling-map-events.md).
- Ensured that MapKit JS shows the same area if a developer uses the same [`CoordinateRegion`](coordinateregion.md) to set the viewable map area during initialization and to later change the viewable map area with [`setRegionAnimated(region, animated)`](map/setregionanimated.md). (Feedback ID: 7626496)

##### 5411

MapKit JS 5.41.1 includes enhancements to the [`Geocoder`](geocoder.md) and [`Search`](search.md) responses, plus bug fixes for rotation events and very large maps.

###### New Features

- [`GeocoderResponse`](geocoderresponse.md) and [`SearchResponse`](searchresponse.md) now return individual address components like `country`, `locality`, and `postCode` in addition to the `formattedAddress` string.

###### Updates

- Fixed rotation issues occurring in unusual circumstances such as setting rotation to infinity and setting rotation multiple times during map initialization.
- Made sure that the map doesn’t encounter errors during panning when displayed fullscreen on very large displays.

##### 5400

MapKit JS 5.40.0 includes bug fixes for event reporting and controls.

###### Updates

- Added asynchronous reporting of failed configuration.
- Improved visibility of map controls in Chrome by decreasing their transparency in Dark Mode.
- Added the ability to reset the map rotation to zero by pressing the spacebar when the compass control has focus.

##### 5390

MapKit JS 5.39.0 includes bug fixes for tile overlays and controls.

###### Updates

- Added the ability to set `tileOverlays` in the `mapkit.Map` constructor.
- Ensured that the Apple Maps logo remains the same size whether the map is in Standard or Hybrid mode.

##### 5381

MapKit JS 5.38.1 includes bug fixes for annotations, annotation clustering, and controls.

###### Updates

- Show default marker annotation appearance (red balloon with a white pin glyph) when the image for an `ImageAnnotation` can’t be found.
- Ensured annotation clustering doesn’t animate if the clusters aren’t visible.
- Ensured that annotation cluster positions stay consistent when zooming.
- Ensured that the Apple logo and Legal link are always visible on the map, even if `padding` has a negative value.

##### 5360

MapKit JS 5.36.0 includes bug fixes.

###### Updates

- Ensured that the `distances` property can be set when creating a new map object. (Feedback ID: 7451047)
- Reworded warnings for `TileOverlay` minimum zoom level.

##### 5350

MapKit JS 5.35.0 includes bug fixes for point-of-interest (POI) Filtering and performance.

###### Updates

- Ensured that `map.pointOfInterestFilter.includesCategory` returns `false` when POI aren’t showing on the map.
- Improved rendering performance when the current location annotation shows on the map.
- Improved panning and zooming performance when there are no annotations on the map.

##### 5342

MapKit JS 5.34.2 includes bug fixes for tile loading, annotations, and map controls.

###### Updates

- Ensured that the map tiles continue to load in cases where the developer initializes the map more than once. (Feedback ID: 7335445)
- Fixed `calloutAppearanceAnimationForAnnotation` for animations on custom callouts.
- Applied a dark style to the current location annotation callout when the map is in dark mode.
- Ensured that the map type control always shows the active map after opening the map type menu.

##### 5331

MapKit JS 5.33.1 includes new APIs for point-of-interest (POI) filtering, plus bug fixes.

###### New Features

- Added new APIs that let a client apply filters to show or hide specific categories of points of interest (POIs) on the map, like “Parks” or “Restaurants”. You can apply these filters to Search and Search Autocomplete results. For more information, see [`What’s New in MapKit and MapKit JS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/236/).

###### Updates

- Adjusted the order of focused controls while tabbing to be more intuitive.
- Ensured that custom annotation callouts apply the `overflow:scroll` style when the developer sets it.
- Ensured that the user location annotation doesn’t overlap other annotations added to the map.
- Prevented marker annotations from being inadvertently styled by CSS in the embedding page.
- Decreased the sensitivity of two-finger zooming to avoid unintentional zooms. For example, a zoom gesture shouldn’t initiate when someone places two fingers on the trackpad.

##### 5322

MapKit JS 5.32.2 includes bug fixes for controls, annotations, and performance.

###### Updates

- Adjusted the position of the Legal link in relation to the user location control.
- Made sure clustered annotations don’t freeze when the user pans or zooms the map with gestures.
- Improved performance by drawing less often.

##### 5301

MapKit JS 5.30.1 includes an improvement to the way marker annotation titles and subtitles render, and minor bug fixes.

###### Updates

- Increased width for marker annotation titles and subtitles so that more text can fit on a single line before breaking.
- Made sure the grab hand cursor shows up when panning a map that is displayed in an HTML `iframe`.

##### 5290

MapKit JS 5.29.0 improves accessibility, performance, and the appearance of controls when they are mirrored for right-to-left languages.

###### Updates

- Improved the performance of [`importGeoJSON(data, callback)`](mapkit/importgeojson.md) by ensuring that the main thread is never blocked.
- Updated controls so that when someone clicks or taps a control that has focus, it retains focus.
- Ensured controls that mirror for right-to-left languages also mirror the pressed state of the zoom buttons.

##### 5281

MapKit JS 5.28.1 improves keyboard navigation, fixes memory leaks, and addresses developer feedback.

###### Updates

- Improved keyboard navigation on the map type control.
- Updated so MapKit JS defaults to HTTPS for CDN connections whenever possible. (Feedback ID: 6790373)
- Fixed a memory leak created when MapKit JS called `destroy()` while the user location error panel was visible.
- Updated the list of POI Filtering categories, removing `ReligiousSite` and `Playground`. POI Filtering ([`What’s New in MapKit and MapKit JS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/236/)) becomes available in the fall of 2019.

##### 5250

MapKit JS 5.25.0 includes various improvements for controls, GeoJSON import, and annotation clusters.

###### Updates

- MapKit JS controls (+/- buttons, compass, Legal link, and so on) are no longer affected by CSS on the enclosing page.
- Updated the Legal link so it connects to HI-IN, IW-IL, and VI-VN localized pages when MapKit JS is running one of these languages.
- Updated spacing on the Apple Maps logo.
- Made various improvements to GeoJSON import, such as adding the ability to handle null geometries in Features, ensuring that an `ItemCollection` is returned even for single item imports, and improving error message reporting.
- Improved clustering behavior when member annotations are on both sides of the antimeridian.
- Ensured that [`annotationsInMapRect(mapRect)`](map/annotationsinmaprect.md) doesn’t return cluster annotations, to match the behavior of [`annotations`](map/annotations.md).

##### 5240

MapKit JS 5.24.0 includes various improvements, including changes to how the Apple Maps logo and Legal link are displayed.

###### Updates

- Improved how marker annotations animate in and out of clusters.
- Improved how annotation clusters are grouped, so that one annotation cluster never overlaps another.
- The [`showItems(items, options)`](map/showitems.md) function now updates the map region in a way that encloses annotation callouts visible on selected annotations, so that any callouts showing aren’t’ cut off the edge of the map.
- The Legal link is now always shown, for all map dimensions.
- The Apple Maps logo in the lower left corner is now displayed on maps with dimensions of 200 x 100 pixels and larger.
- The time to detect a `long-press` map event has been increased to 500 ms. See [`Handling map events`](handling-map-events.md) for more information.
- Improved how [`cameraZoomRange`](map/camerazoomrange.md) and [`cameraBoundary`](map/cameraboundary.md) behave for users in China.

##### 5231

MapKit JS 5.23.1 includes new APIs for region and zoom limits, an updated Apple Maps logo, and more.

###### New Features

- Added the [`cameraDistance`](map/cameradistance.md) property, which sets the altitude of the camera above the center of the map. A change to the map’s camera distance can be animated with [`setCameraDistanceAnimated(distance, animated)`](map/setcameradistanceanimated.md).
- Added the [`cameraZoomRange`](map/camerazoomrange.md) property, which restricts zooming to a specified minimum and maximum camera distance. A change to the map’s camera zoom range can be animated with [`setCameraZoomRangeAnimated(cameraZoomRange, animated)`](map/setcamerazoomrangeanimated.md).
- Added the [`cameraBoundary`](map/cameraboundary.md) property, which restricts panning to a specified coordinate region. A change to the map’s camera boundary can be animated with [`setCameraBoundaryAnimated(mapRect, animated)`](map/setcameraboundaryanimated.md).
- Enabled Directions support for users in China.
- Updated the logo in the lower left corner from the Apple icon to the icon beside the word “Maps”.

###### Updates

- Fixed issue where [`importGeoJSON(data, callback)`](mapkit/importgeojson.md) would not import a `GeometryCollection` nested within a `Feature.`
- Improved how the default marker annotation color is set depending on the map’s [`colorScheme`](map/colorscheme.md). Setting a marker annotation’s color property to `null` sets a default color that matches the current [`colorScheme`](map/colorscheme.md).
- Updated the Legal link on the map to open a web page, instead of displaying a menu.

##### 5220

The MapKit JS 5.22.0 release adds improvements to browser support.

###### New Features

- Added pinch-zoom on trackpad support for Chrome and Firefox.

###### Updates

- Improved performance of mouse wheel zoom for Firefox on Windows.
- Prevented nontouch events from firing during touch gestures in Firefox.

##### 5210

The MapKit JS 5.21.0 release includes a rotation gesture improvement.

###### Updates

- Fixed bug where rotating the map with gesture was not working in Chrome on Android.

##### 5203

The MapKit JS 5.20.3 release includes bug fixes and performance improvements.

###### Updates

- Fixed bug where `https:` was not selected for CDN URLs in some packaged and local environments. (Feedback ID: 48289622)
- Improved annotation CSS to prevent collision with styles on host implementations.
- Improved annotations to warn instead of throw an error in some selection and deselection cases.
- Improved positioning logic for Annotation glyph text.
- Improved performance of annotation image assets.
- Fixed a bug in the callout  where [`glyphImage`](markerannotationconstructoroptions/glyphimage.md) was always used instead of [`selectedGlyphImage`](markerannotation/selectedglyphimage.md) where appropriate.

##### 5191

The MapKit JS 5.19.1 release includes minor fixes and performance improvements.

##### 5180

The MapKit JS 5.18.0 release includes new map interaction events and bug fixes.

###### New Features

- Added map interaction events (single-tap, double-tap, and long-press), which are dispatched by the map when the user does a single tap, a double tap, or a long press, but only when the gesture has no effect on the map (such as selecting an annotation or zooming in).

###### Updates

- Updated the behavior of setters that cause a selection state to change. For example, setting a `selected` property or adding a selected annotation cannot be done within the callback of `select` or `deselect` event listeners. Doing so will throw an error.
- Improved rotation animation when a map has padding.
- Fixed an issue where a [`language`](mapkit/language.md) set by a property (instead of by the [`MapKitInitializationOptions`](mapkitinitializationoptions.md)) would be reset upon initialization.

##### 5171

The MapKit JS 5.17.1 release improves the behavior of rotation when a map has padding.

###### Updates

- Fixed issue where [`rotation`](map/rotation.md) was reset after certain map interactions.
- Fixed compass control to correctly rotate around the center when the map has [`padding`](map/padding.md).

##### 5160

The MapKit JS 5.16.0 release includes new APIs that let developers inset the collision rectangle of annotations.

###### Updates

- Added support for insetting the collision rectangle of annotations with the padding property of Annotations.

##### 5150

The MapKit JS 5.15.0 release includes improvements to the display of annotation and overlay items.

###### Updates

- Improved computation of scale to better respect the padding configuration around items.

##### 5130

MapKit JS 5.13.0 includes new APIs that allow you to present maps in various styles and choose the kind of units in which to display distance.

###### New Features

- Added support for displaying the map in a muted style, which can be enabled by setting the [`mapType`](map/maptype.md) property to [`MutedStandard`](maptype/mutedstandard.md).
- Added support for displaying the map in dark mode, which can be enabled by setting the new [`colorScheme`](map/colorscheme.md) property on the Map object to [`Dark`](colorscheme/dark.md). The default value for [`colorScheme`](map/colorscheme.md) is [`Light`](colorscheme/light.md).
- Added support for customizing the display of distances, as in the scale control. The new [`distances`](map/distances-data.property.md) property on the Map object can be set to [`Metric`](distance/metric.md) or [`Imperial`](distance/imperial.md) to always display metric or imperial units, respectively.

###### Updates

- Improved adaptive behavior of annotations when the map type switches.
- Fixed selection delay for annotations on a map with zoom disabled.

##### 5111

The MapKit JS 5.11.1 release includes bug fixes.

###### Updates

- Cluster annotations display improvements when switching to Hindi and RTL languages.
- Annotations clear from the map immediately when setting the annotations array to `[]`.

##### 5102

The MapKit JS 5.10.2 release includes performance improvements and bug fixes.

###### Updates

- Setting [`isScrollEnabled`](map/isscrollenabled.md) to false can disable scrolling for the enclosing web page on touch devices. (Feedback ID: 45583214)
- `navigator.geolocation.watchPosition` is `undefined`. (Feedback ID: 44311161)
- The Legal link has moved to the bottom-left of the map, next to the Apple logo.
- Improved overall performance when there are hundreds of annotations on the map.
- Improved gesture recognition to prevent accidental rotation.
- Improved VoiceOver support for the compass control.
- Fixed scenario where the compass image was requested too often.
- Fixed zooming, rotation, and panning gestures in Chrome Beta 68.
- Fixed error when map wrapped by a React component is destroyed.

##### 570

MapKit JS 5.7.0 includes minor API changes, support for the new underlying map with Apple data in supported regions, annotation improvements, and more.

This update also introduces a [`MapKit JS Usage Dashboard`](https://developer.apple.comhttps://maps.developer.apple.com) to help monitor API usage against daily limits.

###### New Features

- A new property on the mapkit object named [`maps`](mapkit/maps.md). Map instances are added to this array when they are initialized and removed as soon as they are destroyed.
- [`MapKit JS Usage Dashboard`](https://developer.apple.comhttps://maps.developer.apple.com) that reports the number map initializations and service calls made by your team.

###### Updates

- Added detailed building outlines and parking lots, better road network coverage, and more, in supported areas.
- [`MarkerAnnotation`](markerannotation.md) is updated so that instances with the same [`clusteringIdentifier`](annotation/clusteringidentifier.md) cluster together regardless of their [`displayPriority`](annotationconstructoroptions/displaypriority.md) value.
- When [`displayPriority`](annotation/displaypriority-data.property.md) is set, the animation for the appearance and disappearance of [`MarkerAnnotation`](markerannotation.md) can be triggered. Now, the animation is also triggered when an annotation is hidden by other annotations or when it reappears after a change in zoom level.
- The [`DirectionsResponse`](directionsresponse.md) now includes a [`polyline`](route/polyline.md) property. The value of this property is a [`PolylineOverlay`](polylineoverlay.md), and can be added directly to a map.

###### Deprecated Features

- The path property of the DirectionsResponse is now deprecated in favor of the new polyline property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit-js-5)*
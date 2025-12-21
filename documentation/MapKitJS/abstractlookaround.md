# AbstractLookAround

**Framework**: MapKit JS  
**Kind**: class

An abstract class that provides a common interface for Look Around views.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
abstract class AbstractLookAround extends EventTarget
```

#### Discussion

You can’t initialize an abstract class; use [`LookAround`](lookaround.md) or [`LookAroundPreview`](lookaroundpreview.md) to create a Look Around view.

## Topics

### Static properties
- [ReadyStates](abstractlookaround/readystates.md)
  A static property that allows you to access the Look Around ready-state enumeration.
### Instance Properties
- [element](abstractlookaround/element.md)
  A property that represents the Look Around view’s containing Document Object Model (DOM) element.
- [isNavigationEnabled](abstractlookaround/isnavigationenabled.md)
  A Boolean value that indicates whether someone can navigate inside the Look Around view.
- [isScrollEnabled](abstractlookaround/isscrollenabled.md)
  A Boolean value that indicates whether someone can scroll the Look Around view.
- [isZoomEnabled](abstractlookaround/iszoomenabled.md)
  A Boolean value that indicates whether someone can zoom the Look Around view.
- [openDialog](abstractlookaround/opendialog.md)
  Opens the Look Around view in a dialog.
- [padding](abstractlookaround/padding.md)
  The padding options for the Look Around view.
- [readyState](abstractlookaround/readystate.md)
  A value that represents the loading state of the Look Around object.
- [scene](abstractlookaround/scene.md)
  The Look Around scene the framework is displaying.
- [showsPointsOfInterest](abstractlookaround/showspointsofinterest.md)
  A Boolean value that indicates whether the Look Around view shows points of interest (POIs).
- [showsRoadLabels](abstractlookaround/showsroadlabels.md)
  A Boolean value that indicates whether the Look Around view shows road labels.
### Instance Methods
- [destroy()](abstractlookaround/destroy.md)
  Releases the Look Around view and its resources from memory.

## Relationships

### Inherited By
- [LookAround](lookaround.md)
- [LookAroundPreview](lookaroundpreview.md)

## See Also

- [class LookAround](lookaround.md)
  A view that allows someone to see a street level view of a place.
- [interface LookAroundOptions](lookaroundoptions.md)
  Options for initializing a LookAround view.
- [class LookAroundPreview](lookaroundpreview.md)
  A class that renders a preview of a Look Around view.
- [interface LookAroundPreviewOptions](lookaroundpreviewoptions.md)
  Options for initializing a LookAroundPreview object.
- [class LookAroundScene](lookaroundscene.md)
  Object that represents the current location of the view.
- [interface CommonLookAroundOptions](commonlookaroundoptions.md)
  Options that control the behavior of Look Around views.
- [lookAroundViews](mapkit/lookaroundviews.md)
  A list of all the Look Around objects that are currently active on a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/abstractlookaround)*
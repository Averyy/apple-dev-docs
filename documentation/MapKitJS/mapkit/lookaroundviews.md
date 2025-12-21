# lookAroundViews

**Framework**: MapKit JS  
**Kind**: property

A list of all the Look Around objects that are currently active on a page.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get lookAroundViews(): AbstractLookAround[];
```

#### Discussion

You must load the appropriate library before accessing the property, otherwise, the property throws an `Error`.

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
- [class AbstractLookAround](abstractlookaround.md)
  An abstract class that provides a common interface for Look Around views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit/lookaroundviews)*
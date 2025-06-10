# showTripPreviews(_:selectedTrip:textConfiguration:)

**Framework**: CarPlay  
**Kind**: method

Displays the previews for a collection of trips, with a single selected trip.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
func showTripPreviews(_ tripPreviews: [CPTrip], selectedTrip: CPTrip?, textConfiguration: CPTripPreviewTextConfiguration?)
```

#### Discussion

Use this method to display upcoming trips or multiple trip options, such as search results. Trip previews can appear over an active navigation session. Provide an array of up to twelve [`CPTrip`](cptrip.md) objects to preview. If the array contains more objects, CarPlay displays only the first twelve.

The trip you want to select must be a member of the `tripPreviews` array.

## Parameters

- `tripPreviews`: An array of trips to preview.
- `selectedTrip`: The trip to select when CarPlay presents the list of trip previews.
- `textConfiguration`: A configuration object that contains the various titles a trip preview button can display.

## See Also

- [func showTripPreviews([CPTrip], textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showtrippreviews(_:textconfiguration:).md)
  Displays the preview for one or more trips, and allows route selection.
- [func hideTripPreviews()](cpmaptemplate/hidetrippreviews.md)
  Hides the display of trip previews.
- [func showRouteChoicesPreview(for: CPTrip, textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showroutechoicespreview(for:textconfiguration:).md)
  Displays the route choices for a single trip.
- [class CPTripPreviewTextConfiguration](cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/showtrippreviews(_:selectedtrip:textconfiguration:))*
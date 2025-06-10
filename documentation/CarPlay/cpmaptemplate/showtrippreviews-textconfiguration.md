# showTripPreviews(_:textConfiguration:)

**Framework**: CarPlay  
**Kind**: method

Displays the preview for one or more trips, and allows route selection.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func showTripPreviews(_ tripPreviews: [CPTrip], textConfiguration: CPTripPreviewTextConfiguration?)
```

#### Discussion

Use this method to display upcoming trips or multiple trip options, such as for search results. Trip previews can appear over the active navigation session.

## Parameters

- `tripPreviews`: A list of trips to preview, limited to 12 trips.
- `textConfiguration`: A text configuration object containing the titles to display on trip preview buttons.

## See Also

- [func showTripPreviews([CPTrip], selectedTrip: CPTrip?, textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showtrippreviews(_:selectedtrip:textconfiguration:).md)
  Displays the previews for a collection of trips, with a single selected trip.
- [func hideTripPreviews()](cpmaptemplate/hidetrippreviews.md)
  Hides the display of trip previews.
- [func showRouteChoicesPreview(for: CPTrip, textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showroutechoicespreview(for:textconfiguration:).md)
  Displays the route choices for a single trip.
- [class CPTripPreviewTextConfiguration](cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/showtrippreviews(_:textconfiguration:))*
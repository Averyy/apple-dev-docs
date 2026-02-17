# showRouteChoicesPreview(for:textConfiguration:)

**Framework**: CarPlay  
**Kind**: method

Displays the route choices for a single trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func showRouteChoicesPreview(for tripPreview: CPTrip, textConfiguration: CPTripPreviewTextConfiguration?)
```

#### Discussion

The trip preview can appear over an active navigation session.

## Parameters

- `tripPreview`: The trip to preview.
- `textConfiguration`: A text configuration object containing the titles to display on trip preview buttons.

## See Also

- [func showTripPreviews([CPTrip], textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showtrippreviews(_:textconfiguration:).md)
  Displays the preview for one or more trips, and allows route selection.
- [func showTripPreviews([CPTrip], selectedTrip: CPTrip?, textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showtrippreviews(_:selectedtrip:textconfiguration:).md)
  Displays the previews for a collection of trips, with a single selected trip.
- [func hideTripPreviews()](cpmaptemplate/hidetrippreviews.md)
  Hides the display of trip previews.
- [class CPTripPreviewTextConfiguration](cptrippreviewtextconfiguration.md)
  A configuration object for changing the button titles on a trip preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/showroutechoicespreview(for:textconfiguration:))*
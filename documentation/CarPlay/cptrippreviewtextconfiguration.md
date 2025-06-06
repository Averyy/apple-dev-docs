# CPTripPreviewTextConfiguration

**Framework**: CarPlay  
**Kind**: class

A configuration object for changing the button titles on a trip preview.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPTripPreviewTextConfiguration
```

## Topics

### Creating a Text Configuration Object
- [init(startButtonTitle: String?, additionalRoutesButtonTitle: String?, overviewButtonTitle: String?)](cptrippreviewtextconfiguration/init(startbuttontitle:additionalroutesbuttontitle:overviewbuttontitle:).md)
  Creates a trip preview text configuration object.
### Setting Button Titles
- [var startButtonTitle: String?](cptrippreviewtextconfiguration/startbuttontitle.md)
  The title displayed on the start button.
- [var additionalRoutesButtonTitle: String?](cptrippreviewtextconfiguration/additionalroutesbuttontitle.md)
  The title displayed on the routes button.
- [var overviewButtonTitle: String?](cptrippreviewtextconfiguration/overviewbuttontitle.md)
  The title displayed on the overview button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func showTripPreviews([CPTrip], textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showtrippreviews(_:textconfiguration:).md)
  Displays the preview for one or more trips, and allows route selection.
- [func showTripPreviews([CPTrip], selectedTrip: CPTrip?, textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showtrippreviews(_:selectedtrip:textconfiguration:).md)
  Displays the previews for a collection of trips, with a single selected trip.
- [func hideTripPreviews()](cpmaptemplate/hidetrippreviews.md)
  Hides the display of trip previews.
- [func showRouteChoicesPreview(for: CPTrip, textConfiguration: CPTripPreviewTextConfiguration?)](cpmaptemplate/showroutechoicespreview(for:textconfiguration:).md)
  Displays the route choices for a single trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrippreviewtextconfiguration)*
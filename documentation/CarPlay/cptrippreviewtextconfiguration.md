# CPTripPreviewTextConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A configuration object for changing the button titles on a trip preview.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPTripPreviewTextConfiguration
```

```objc
@interface CPTripPreviewTextConfiguration : NSObject
```

## Topics

### Creating a Text Configuration Object
- [init(startButtonTitle: String?, additionalRoutesButtonTitle: String?, overviewButtonTitle: String?)](./cptrippreviewtextconfiguration/init%28startbuttontitle,additionalroutesbuttontitle,overviewbuttontitle%29.md)
  Creates a trip preview text configuration object.
### Setting Button Titles
- [var startButtonTitle: String?](./cptrippreviewtextconfiguration/startbuttontitle.md)
  The title displayed on the start button.
- [var additionalRoutesButtonTitle: String?](./cptrippreviewtextconfiguration/additionalroutesbuttontitle.md)
  The title displayed on the routes button.
- [var overviewButtonTitle: String?](./cptrippreviewtextconfiguration/overviewbuttontitle.md)
  The title displayed on the overview button.
### Initializers
- [init?(coder: NSCoder)](./cptrippreviewtextconfiguration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Displaying Trip Previews
- [func showTripPreviews([CPTrip], textConfiguration: CPTripPreviewTextConfiguration?)](./cpmaptemplate/showtrippreviews%28_,textconfiguration%29.md)
  Displays the preview for one or more trips, and allows route selection.
- [func showTripPreviews([CPTrip], selectedTrip: CPTrip?, textConfiguration: CPTripPreviewTextConfiguration?)](./cpmaptemplate/showtrippreviews%28_,selectedtrip,textconfiguration%29.md)
  Displays the previews for a collection of trips, with a single selected trip.
- [func hideTripPreviews()](./cpmaptemplate/hidetrippreviews%28%29.md)
  Hides the display of trip previews.
- [func showRouteChoicesPreview(for: CPTrip, textConfiguration: CPTripPreviewTextConfiguration?)](./cpmaptemplate/showroutechoicespreview%28for,textconfiguration%29.md)
  Displays the route choices for a single trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrippreviewtextconfiguration)*
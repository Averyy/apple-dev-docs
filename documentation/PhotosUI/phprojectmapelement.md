# PHProjectMapElement

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An element that represents a map within project section content.

**Availability**:
- macOS 10.14+

## Declaration

```swift
class PHProjectMapElement
```

```objc
@interface PHProjectMapElement : PHProjectElement
```

## Topics

### Pinpointing the Map
- [var mapType: MKMapType](./phprojectmapelement/maptype.md)
  The type of map in the project.
- [var centerCoordinate: CLLocationCoordinate2D](./phprojectmapelement/centercoordinate.md)
  The coordinates of the center of the map.
- [var heading: CLLocationDirection](./phprojectmapelement/heading.md)
  The heading of the map.
- [var pitch: CGFloat](./phprojectmapelement/pitch.md)
  The pitch of the map.
- [var altitude: CLLocationDistance](./phprojectmapelement/altitude.md)
  The altitude of the map.
- [var annotations: [any MKAnnotation]](./phprojectmapelement/annotations.md)
  An array of optional annotations attached to the map.

## Relationships

### Inherits From
- [PHProjectElement](./phprojectelement.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Subclassing Project Elements
- [class PHProjectAssetElement](./phprojectassetelement.md)
  An element that represents a media asset within project section content.
- [class PHProjectTextElement](./phprojecttextelement.md)
  An element that represents text within project section content.
- [class PHProjectJournalEntryElement](./phprojectjournalentryelement.md)
  An element that represents a journal entry within project section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectmapelement)*
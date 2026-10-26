# PHProjectJournalEntryElement

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An element that represents a journal entry within project section content.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectJournalEntryElement
```

```objc
@interface PHProjectJournalEntryElement : PHProjectElement
```

## Topics

### Describing a Journal Entry
- [var date: Date](./phprojectjournalentryelement/date.md)
  The date of the journal entry.
- [var assetElement: PHProjectAssetElement?](./phprojectjournalentryelement/assetelement.md)
  An optional asset to represent the date in the journal entry.
- [var textElement: PHProjectTextElement?](./phprojectjournalentryelement/textelement.md)
  Descriptive text for the date of the entry.

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
- [class PHProjectMapElement](./phprojectmapelement.md)
  An element that represents a map within project section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectjournalentryelement)*
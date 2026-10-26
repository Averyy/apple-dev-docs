# PHProjectTextElement

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An element that represents text within project section content.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectTextElement
```

```objc
@interface PHProjectTextElement : PHProjectElement
```

## Topics

### Describing a Text Element
- [var text: String](./phprojecttextelement/text.md)
  The raw unformatted string for the text element.
- [var attributedText: NSAttributedString?](./phprojecttextelement/attributedtext.md)
  The stylized attributed string for the text element as presented to the user in Photos.
- [var textElementType: PHProjectTextElement.ElementType](./phprojecttextelement/textelementtype.md)
  The enumerated type of the text element.
- [PHProjectTextElement.ElementType](./phprojecttextelement/elementtype.md)
  An enumeration of the type of text element.

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
- [class PHProjectJournalEntryElement](./phprojectjournalentryelement.md)
  An element that represents a journal entry within project section content.
- [class PHProjectMapElement](./phprojectmapelement.md)
  An element that represents a map within project section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttextelement)*
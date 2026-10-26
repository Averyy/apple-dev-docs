# PHProjectTextElement.ElementType

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

An enumeration of the type of text element.

**Availability**:
- macOS 10.13+

## Declaration

```swift
enum ElementType
```

```c
enum PHProjectTextElementType : NSInteger;
```

## Topics

### Types of Text Elements
- [PHProjectTextElement.ElementType.body](./elementtype/body.md)
  An enumeration to denote body text.
- [PHProjectTextElement.ElementType.title](./elementtype/title.md)
  An enumeration to denote title text in the header view.
- [PHProjectTextElement.ElementType.subtitle](./elementtype/subtitle.md)
  An enumeration to denote subtitle text in the header view.
### Initializers
- [init?(rawValue: Int)](./elementtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing a Text Element
- [var text: String](./text.md)
  The raw unformatted string for the text element.
- [var attributedText: NSAttributedString?](./attributedtext.md)
  The stylized attributed string for the text element as presented to the user in Photos.
- [var textElementType: PHProjectTextElement.ElementType](./textelementtype.md)
  The enumerated type of the text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttextelement/elementtype)*
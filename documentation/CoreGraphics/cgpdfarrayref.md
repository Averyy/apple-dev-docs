# CGPDFArrayRef

**Framework**: Core Graphics  
**Kind**: struct

An opaque type that encapsulates a PDF array.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CGPDFArrayRef
```

## Topics

### Initializers
- [init(OpaquePointer)](cgpdfarrayref/init(_:).md)
- [init(rawValue: OpaquePointer)](cgpdfarrayref/init(rawvalue:).md)
### Instance Methods
- [func array(at: Int) -> CGPDFArrayRef?](cgpdfarrayref/array(at:).md)
- [func boolean(at: Int) -> Bool?](cgpdfarrayref/boolean(at:).md)
- [func dictionary(at: Int) -> CGPDFDictionaryRef?](cgpdfarrayref/dictionary(at:).md)
- [func enumerateObjects((Int, CGPDFObjectRef) -> Bool)](cgpdfarrayref/enumerateobjects(_:).md)
- [func integer(at: Int) -> Int?](cgpdfarrayref/integer(at:).md)
- [func name(at: Int) -> String?](cgpdfarrayref/name(at:).md)
- [func number(at: Int) -> Double?](cgpdfarrayref/number(at:).md)
- [func stream(at: Int) -> CGPDFStreamRef?](cgpdfarrayref/stream(at:).md)
- [func string(at: Int) -> CGPDFStringRef?](cgpdfarrayref/string(at:).md)
### Subscripts
- [subscript(Int, String.Type) -> String?](cgpdfarrayref/subscript(_:_:)-2eokv.md)
- [subscript(Int, Bool.Type) -> Bool?](cgpdfarrayref/subscript(_:_:)-3u09c.md)
- [subscript(Int, CGPDFDictionaryRef.Type) -> CGPDFDictionaryRef?](cgpdfarrayref/subscript(_:_:)-6ku0l.md)
- [subscript(Int, Double.Type) -> Double?](cgpdfarrayref/subscript(_:_:)-6nppv.md)
- [subscript(Int, CGPDFStringRef.Type) -> CGPDFStringRef?](cgpdfarrayref/subscript(_:_:)-7azm2.md)
- [subscript(Int, CGPDFStreamRef.Type) -> CGPDFStreamRef?](cgpdfarrayref/subscript(_:_:)-86xex.md)
- [subscript(Int, Int.Type) -> Int?](cgpdfarrayref/subscript(_:_:)-8g5vk.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [PDFObjectType](pdfobjecttype.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfarrayref)*
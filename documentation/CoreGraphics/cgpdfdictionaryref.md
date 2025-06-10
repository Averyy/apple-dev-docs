# CGPDFDictionaryRef

**Framework**: Core Graphics  
**Kind**: struct

A type that encapsulates a PDF dictionary.

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
struct CGPDFDictionaryRef
```

## Topics

### Initializers
- [init(OpaquePointer)](cgpdfdictionaryref/init(_:).md)
- [init(rawValue: OpaquePointer)](cgpdfdictionaryref/init(rawvalue:).md)
### Instance Methods
- [func array(forKey: String) -> CGPDFArrayRef?](cgpdfdictionaryref/array(forkey:).md)
- [func boolean(forKey: String) -> Bool?](cgpdfdictionaryref/boolean(forkey:).md)
- [func count() -> Int](cgpdfdictionaryref/count.md)
- [func dictionary(forKey: String) -> CGPDFDictionaryRef?](cgpdfdictionaryref/dictionary(forkey:).md)
- [func enumerateObjects((String, CGPDFObjectRef) -> Bool)](cgpdfdictionaryref/enumerateobjects(_:).md)
- [func integer(forKey: String) -> Int?](cgpdfdictionaryref/integer(forkey:).md)
- [func name(forKey: String) -> String?](cgpdfdictionaryref/name(forkey:).md)
- [func number(forKey: String) -> Double?](cgpdfdictionaryref/number(forkey:).md)
- [func object(forKey: String) -> CGPDFObjectRef?](cgpdfdictionaryref/object(forkey:).md)
- [func stream(forKey: String) -> CGPDFStreamRef?](cgpdfdictionaryref/stream(forkey:).md)
- [func string(forKey: String) -> CGPDFStringRef?](cgpdfdictionaryref/string(forkey:).md)
### Subscripts
- [subscript(String) -> (any PDFObjectType)?](cgpdfdictionaryref/subscript(_:).md)
- [subscript(String, CGPDFStreamRef.Type) -> CGPDFStreamRef?](cgpdfdictionaryref/subscript(_:_:)-1ggo7.md)
- [subscript(String, CGPDFDictionaryRef.Type) -> CGPDFDictionaryRef?](cgpdfdictionaryref/subscript(_:_:)-2brm1.md)
- [subscript(String, Int.Type) -> Int?](cgpdfdictionaryref/subscript(_:_:)-4ukiv.md)
- [subscript(String, String.Type) -> String?](cgpdfdictionaryref/subscript(_:_:)-7n16o.md)
- [subscript(String, Bool.Type) -> Bool?](cgpdfdictionaryref/subscript(_:_:)-8vekr.md)
- [subscript(String, Double.Type) -> Double?](cgpdfdictionaryref/subscript(_:_:)-9njdk.md)
- [subscript(String, CGPDFStringRef.Type) -> CGPDFStringRef?](cgpdfdictionaryref/subscript(_:_:)-y8tv.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [PDFObjectType](pdfobjecttype.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdictionaryref)*
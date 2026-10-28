# notationName

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the name of the notation associated with the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var notationName: String? { get set }
```

```objc
@property (copy, nullable) NSString * notationName;
```

## Return Value

The name of the notation associated with the receiver.

## Discussion

Notations are applicable to unparsed external entities, processing instructions, and some attribute values.

## See Also

### Managing DTD Identifiers
- [var isExternal: Bool](./isexternal.md)
  True if the system id is set. Valid for entities and notations.
- [var publicID: String?](./publicid.md)
  Returns the public identifier associated with the receiver.
- [var systemID: String?](./systemid.md)
  Returns the system identifier associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/notationname)*
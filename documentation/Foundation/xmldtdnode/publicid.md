# publicID

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the public identifier associated with the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var publicID: String? { get set }
```

```objc
@property (copy, nullable) NSString * publicID;
```

#### Return Value

The public identifier associated with the receiver.

#### Discussion

The public ID is applicable to entities and notations.

## See Also

### Managing DTD Identifiers
- [var isExternal: Bool](./isexternal.md)
  True if the system id is set. Valid for entities and notations.
- [var notationName: String?](./notationname.md)
  Returns the name of the notation associated with the receiver.
- [var systemID: String?](./systemid.md)
  Returns the system identifier associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/publicid)*
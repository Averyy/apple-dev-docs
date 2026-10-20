# isExternal

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

True if the system id is set. Valid for entities and notations.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var isExternal: Bool { get }
```

```objc
@property (readonly, getter=isExternal) BOOL external;
```

## See Also

### Managing DTD Identifiers
- [var notationName: String?](./notationname.md)
  Returns the name of the notation associated with the receiver.
- [var publicID: String?](./publicid.md)
  Returns the public identifier associated with the receiver.
- [var systemID: String?](./systemid.md)
  Returns the system identifier associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/isexternal)*
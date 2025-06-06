# formats

**Framework**: Core Media I/O  
**Kind**: property  
**Required**: Yes

An array of formats that a stream supports.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var formats: [CMIOExtensionStreamFormat] { get }
```

#### Discussion

Don’t change stream formats during the life cycle of the associated stream.

## See Also

- [class CMIOExtensionStreamFormat](cmioextensionstreamformat.md)
  An object that describes the format of a media stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/formats)*
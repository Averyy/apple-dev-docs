# formats

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array of formats that a stream supports.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var formats: [CMIOExtensionStreamFormat] { get }
```

```objc
@property (atomic, readonly) NSArray<CMIOExtensionStreamFormat *> * formats;
```

#### Discussion

Don’t change stream formats during the life cycle of the associated stream.

## See Also

### Accessing the Source Format
- [class CMIOExtensionStreamFormat](../cmioextensionstreamformat.md)
  An object that describes the format of a media stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/formats)*
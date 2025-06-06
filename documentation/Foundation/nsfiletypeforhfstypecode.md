# NSFileTypeForHFSTypeCode(_:)

**Framework**: Foundation  
**Kind**: func

Returns a string encoding a file type code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSFileTypeForHFSTypeCode(_ hfsFileTypeCode: OSType) -> String!
```

#### Return Value

A string that encodes `hfsFileTypeCode`.

## Parameters

- `hfsFileTypeCode`: An HFS file type code.

## See Also

- [func NSHFSTypeCodeFromFileType(String!) -> OSType](nshfstypecodefromfiletype(_:).md)
  Returns a file type code.
- [func NSHFSTypeOfFile(String!) -> String!](nshfstypeoffile(_:).md)
  Returns a string encoding a file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfiletypeforhfstypecode(_:))*
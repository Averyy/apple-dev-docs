# NSHFSTypeCodeFromFileType(_:)

**Framework**: Foundation  
**Kind**: func

Returns a file type code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSHFSTypeCodeFromFileType(_ fileTypeString: String!) -> OSType
```

#### Return Value

The HFS file type code corresponding to `fileTypeString`, or `0` if it cannot be found.

## Parameters

- `fileTypeString`: A string of the sort encoded by  .

## See Also

- [func NSFileTypeForHFSTypeCode(OSType) -> String!](nsfiletypeforhfstypecode(_:).md)
  Returns a string encoding a file type code.
- [func NSHFSTypeOfFile(String!) -> String!](nshfstypeoffile(_:).md)
  Returns a string encoding a file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshfstypecodefromfiletype(_:))*
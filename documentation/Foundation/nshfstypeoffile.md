# NSHFSTypeOfFile(_:)

**Framework**: Foundation  
**Kind**: func

Returns a string encoding a file type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSHFSTypeOfFile(_ fullFilePath: String!) -> String!
```

#### Return Value

A string that encodes `fullFilePath`’s HFS file type, or `nil` if the operation was not successful

## Parameters

- `fullFilePath`: The full absolute path of a file.

## See Also

- [func NSFileTypeForHFSTypeCode(OSType) -> String!](nsfiletypeforhfstypecode(_:).md)
  Returns a string encoding a file type code.
- [func NSHFSTypeCodeFromFileType(String!) -> OSType](nshfstypecodefromfiletype(_:).md)
  Returns a file type code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshfstypeoffile(_:))*
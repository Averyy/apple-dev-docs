# NSHFSTypeCodeFromFileType(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a file type code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSHFSTypeCodeFromFileType(_ fileTypeString: String!) -> OSType
```

```c
extern OSType NSHFSTypeCodeFromFileType(NSString *fileTypeString);
```

## Return Value

The HFS file type code corresponding to `fileTypeString`, or `0` if it cannot be found.

## Parameters

- `fileTypeString`: A string of the sort encoded by `NSFileTypeForHFSTypeCode()`.

## See Also

### Working with HFS file types
- [func NSFileTypeForHFSTypeCode(OSType) -> String!](./nsfiletypeforhfstypecode%28_%29.md)
  Returns a string encoding a file type code.
- [func NSHFSTypeOfFile(String!) -> String!](./nshfstypeoffile%28_%29.md)
  Returns a string encoding a file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshfstypecodefromfiletype(_:))*
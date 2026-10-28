# NSFileTypeForHFSTypeCode(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a string encoding a file type code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSFileTypeForHFSTypeCode(_ hfsFileTypeCode: OSType) -> String!
```

```c
extern NSString *NSFileTypeForHFSTypeCode(OSType hfsFileTypeCode);
```

## Return Value

A string that encodes `hfsFileTypeCode`.

## Parameters

- `hfsFileTypeCode`: An HFS file type code.

## See Also

### Working with HFS file types
- [func NSHFSTypeCodeFromFileType(String!) -> OSType](./nshfstypecodefromfiletype%28_%29.md)
  Returns a file type code.
- [func NSHFSTypeOfFile(String!) -> String!](./nshfstypeoffile%28_%29.md)
  Returns a string encoding a file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfiletypeforhfstypecode(_:))*
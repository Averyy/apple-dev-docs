# supportedXattrNames(for:)

**Framework**: FSKit  
**Kind**: method

Returns an array that specifies the extended attribute names the given item supports.

**Availability**:
- macOS 15.4+

## Declaration

```swift
optional func supportedXattrNames(for item: FSItem) -> [FSFileName]
```

#### Discussion

If `item` supports no extended attributes, this method returns `nil`.

Only implement this method if your volume works with “limited” extended attributes. For purposes of this protocol, “limited” support means the volume doesn’t support extended attributes generally, but uses these APIs to expose specific file system data.

> **Note**: If a file system implements this method, FSKit assumes limited support for extended attributes exists. In this mode, FSkit only calls this protocol’s methods for the extended attribute names this method returns.

## Parameters

- `item`: The item for which to get information.

## See Also

- [FSVolume.SetXattrPolicy](fsvolume/setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/supportedxattrnames(for:))*
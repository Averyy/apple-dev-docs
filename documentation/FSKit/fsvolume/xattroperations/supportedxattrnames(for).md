# supportedXattrNames(for:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Returns an array that specifies the extended attribute names the given item supports.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
optional func supportedXattrNames(for item: FSItem) -> [FSFileName]
```

```objc
- (NSArray<FSFileName *> *) supportedXattrNamesForItem:(FSItem *) item;
```

#### Discussion

If `item` supports no extended attributes, this method returns `nil`.

Only implement this method if your volume works with “limited” extended attributes. For purposes of this protocol, “limited” support means the volume doesn’t support extended attributes generally, but uses these APIs to expose specific file system data.

> **Note**: If a file system implements this method, FSKit assumes limited support for extended attributes exists. In this mode, FSkit only calls this protocol’s methods for the extended attribute names this method returns.

## Parameters

- `item`: The item for which to get information.

## See Also

### Reading and writing
- [func getXattr(named: FSFileName, of: FSItem, replyHandler: (Data?, (any Error)?) -> Void)](./getxattr%28named,of,replyhandler%29.md)
  Gets the specified extended attribute of the given item.
- [func listXattrs(of: FSItem, replyHandler: ([FSFileName]?, (any Error)?) -> Void)](./listxattrs%28of,replyhandler%29.md)
  Gets the list of extended attributes currently set on the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler: ((any Error)?) -> Void)](./setxattr%28named,to,on,policy,replyhandler%29.md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](../setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/supportedxattrnames(for:))*
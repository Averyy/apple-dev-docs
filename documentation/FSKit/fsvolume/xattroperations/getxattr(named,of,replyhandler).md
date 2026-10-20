# getXattr(named:of:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the specified extended attribute of the given item.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func getXattr(named name: FSFileName, of item: FSItem, replyHandler reply: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func xattr(named name: FSFileName, of item: FSItem) async throws -> Data
```

```objc
- (void) getXattrNamed:(FSFileName *) name ofItem:(FSItem *) item replyHandler:(void (^)(NSData *value, NSError *error)) reply;
```

## Parameters

- `name`: The extended attribute name.
- `item`: The item for which to get the extended attribute.
- `reply`: A block or closure to indicate success or failure. If getting the attribute succeeds, pass an data instance containing the extended attribute data and a `nil` error. If getting the attribute fails, pass the relevant error as the second parameter; FSKit ignores any data in this case. For an `async` Swift implementation, there’s no reply handler; simply return the data or throw an error.

## See Also

### Reading and writing
- [func listXattrs(of: FSItem, replyHandler: ([FSFileName]?, (any Error)?) -> Void)](./listxattrs%28of,replyhandler%29.md)
  Gets the list of extended attributes currently set on the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler: ((any Error)?) -> Void)](./setxattr%28named,to,on,policy,replyhandler%29.md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](../setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](./supportedxattrnames%28for%29.md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/getxattr(named:of:replyhandler:))*
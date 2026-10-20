# listXattrs(of:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the list of extended attributes currently set on the given item.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func listXattrs(of item: FSItem, replyHandler reply: @escaping @Sendable ([FSFileName]?, (any Error)?) -> Void)
```

```swift
func xattrs(of item: FSItem) async throws -> [FSFileName]
```

```objc
- (void) listXattrsOfItem:(FSItem *) item replyHandler:(void (^)(NSArray<FSFileName *> *value, NSError *error)) reply;
```

## Parameters

- `item`: The item from which to get extended attributes.
- `reply`: A block or closure to indicate success or failure. If getting the list of extended attributes succeeds, pass the xattrs as an array of [`FSFileName`](../../fsfilename.md) instances and a `nil` error. If getting the attributes fails, pass `nil` along with the relevant error. For an `async` Swift implementation, there’s no reply handler; simply return the byte count or throw an error.

## See Also

### Reading and writing
- [func getXattr(named: FSFileName, of: FSItem, replyHandler: (Data?, (any Error)?) -> Void)](./getxattr%28named,of,replyhandler%29.md)
  Gets the specified extended attribute of the given item.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler: ((any Error)?) -> Void)](./setxattr%28named,to,on,policy,replyhandler%29.md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](../setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](./supportedxattrnames%28for%29.md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/listxattrs(of:replyhandler:))*
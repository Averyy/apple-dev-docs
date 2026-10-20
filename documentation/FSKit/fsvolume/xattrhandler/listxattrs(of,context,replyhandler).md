# listXattrs(of:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the list of extended attributes currently set on the given item.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func listXattrs(of item: FSItem, context: FSContext, replyHandler reply: @escaping @Sendable (FSListXattrsResult?, (any Error)?) -> Void)
```

```swift
func xattrs(of item: FSItem, context: FSContext) async throws -> FSListXattrsResult
```

```objc
- (void) listXattrsOfItem:(FSItem *) item context:(FSContext *) context replyHandler:(void (^)(FSListXattrsResult *result, NSError *error)) reply;
```

## Parameters

- `item`: The item from which to get extended attributes.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If getting the list of extended attributes succeeds, pass an instance of [`FSListXattrsResult`](../../fslistxattrsresult.md) containing the xattrs as an array of [`FSFileName`](../../fsfilename.md) instances, along with a `nil` error. If getting the attributes fails, pass the relevant error as the second parameter; FSKit ignores the [`FSListXattrsResult`](../../fslistxattrsresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

### Reading and writing
- [func getXattr(named: FSFileName, of: FSItem, context: FSContext, replyHandler: (FSGetXattrResult?, (any Error)?) -> Void)](./getxattr%28named,of,context,replyhandler%29.md)
  Gets the specified extended attribute of the given item.
- [class FSGetXattrResult](../../fsgetxattrresult.md)
  The result of a get-extended-attributes call.
- [class FSListXattrsResult](../../fslistxattrsresult.md)
  The result of a list-extended-attributes call.
- [func setXattr(named: FSFileName, to: Data?, on: FSItem, policy: FSVolume.SetXattrPolicy, context: FSContext, replyHandler: (FSSetXattrResult?, (any Error)?) -> Void)](./setxattr%28named,to,on,policy,context,replyhandler%29.md)
  Sets the specified extended attribute data on the given item.
- [FSVolume.SetXattrPolicy](../setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [class FSSetXattrResult](../../fssetxattrresult.md)
  The result of a set-extended-attributes call.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](./supportedxattrnames%28for%29.md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattrhandler/listxattrs(of:context:replyhandler:))*
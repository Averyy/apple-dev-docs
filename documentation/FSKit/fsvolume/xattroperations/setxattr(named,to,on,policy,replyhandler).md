# setXattr(named:to:on:policy:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the specified extended attribute data on the given item.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func setXattr(named name: FSFileName, to value: Data?, on item: FSItem, policy: FSVolume.SetXattrPolicy, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setXattr(named name: FSFileName, to value: Data?, on item: FSItem, policy: FSVolume.SetXattrPolicy) async throws
```

```objc
- (void) setXattrNamed:(FSFileName *) name toData:(NSData *) value onItem:(FSItem *) item policy:(FSSetXattrPolicy) policy replyHandler:(void (^)(NSError *error)) reply;
```

## Parameters

- `name`: The extended attribute name.
- `value`: The extended attribute value to set. This can’t be `nil`, unless the policy is [`FSVolume.SetXattrPolicy.delete`](../setxattrpolicy/delete.md).
- `item`: The item on which to set the extended attribute.
- `policy`: The policy to apply when setting the attribute. See [`FSVolume.SetXattrPolicy`](../setxattrpolicy.md) for possible values.
- `reply`: A block or closure to indicate success or failure. If setting the attribute fails, pass an error as the one parameter to the reply handler. If setting the attribute succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

### Reading and writing
- [func getXattr(named: FSFileName, of: FSItem, replyHandler: (Data?, (any Error)?) -> Void)](./getxattr%28named,of,replyhandler%29.md)
  Gets the specified extended attribute of the given item.
- [func listXattrs(of: FSItem, replyHandler: ([FSFileName]?, (any Error)?) -> Void)](./listxattrs%28of,replyhandler%29.md)
  Gets the list of extended attributes currently set on the given item.
- [FSVolume.SetXattrPolicy](../setxattrpolicy.md)
  Flags to specify the policy when setting extended file attributes.
- [func supportedXattrNames(for: FSItem) -> [FSFileName]](./supportedxattrnames%28for%29.md)
  Returns an array that specifies the extended attribute names the given item supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/setxattr(named:to:on:policy:replyhandler:))*
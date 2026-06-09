# setXattr(named:to:on:policy:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Sets the specified extended attribute data on the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func setXattr(named name: FSFileName, to value: Data?, on item: FSItem, policy: FSVolume.SetXattrPolicy) async throws
```

## Parameters

- `name`: The extended attribute name.
- `value`: The extended attribute value to set. This can’t be `nil`, unless the policy is [`FSVolume.SetXattrPolicy.delete`](fsvolume/setxattrpolicy/delete.md).
- `item`: The item on which to set the extended attribute.
- `policy`: The policy to apply when setting the attribute. See [`FSVolume.SetXattrPolicy`](fsvolume/setxattrpolicy.md) for possible values.
- `reply`: A block or closure to indicate success or failure. If setting the attribute fails, pass an error as the one parameter to the reply handler. If setting the attribute succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/xattroperations/setxattr(named:to:on:policy:replyhandler:))*
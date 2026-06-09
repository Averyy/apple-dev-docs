# content

**Framework**: Accessory Live Activities  
**Kind**: property

The updated content of the forwarded Live Activity.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
let content: AccessoryLiveActivity.Content?
```

#### Overview

If a Live Activity update only changes the activity’s [`state`](accessoryliveactivity/state.md) and doesn’t contain updated data, the `content` property is `nil`. If the `content` property isn’t `nil`, check the [`alert`](accessoryliveactivity/content-swift.struct/alert.md) to determine whether the update requires you to render a notification-style alert on your accessory.

## See Also

- [let state: ActivityState](accessoryliveactivity/state.md)
  The current state of the activity in its life cycle.
- [AccessoryLiveActivity.Content](accessoryliveactivity/content-swift.struct.md)
  The content of an alert for a forwarded Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/accessoryliveactivity/content-swift.property)*
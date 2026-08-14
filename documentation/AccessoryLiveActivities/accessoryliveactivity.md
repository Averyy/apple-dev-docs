# AccessoryLiveActivity

**Framework**: Accessory Live Activities  
**Kind**: struct

The details of the Live Activity that iOS forwards to your accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
struct AccessoryLiveActivity
```

## Mentions

- [Receiving Live Activity updates and alerts on an accessory](receiving-live-activities-on-an-accessory.md)

## Topics

### Identifying the activity
- [let activityIdentifier: String](accessoryliveactivity/activityidentifier.md)
  A string that uniquely identifies the Live Activity.
- [let sourceBundleIdentifier: String](accessoryliveactivity/sourcebundleidentifier.md)
  The bundle identifier of the app that started the Live Activity.
- [let sourceBundleName: String](accessoryliveactivity/sourcebundlename.md)
  The name of the app from which the activity content originated.
### Accessing the activity’s state and content
- [let state: ActivityState](accessoryliveactivity/state.md)
  The current state of the activity in its life cycle.
- [let content: AccessoryLiveActivity.Content?](accessoryliveactivity/content-swift.property.md)
  The updated content of the forwarded Live Activity.
- [AccessoryLiveActivity.Content](accessoryliveactivity/content-swift.struct.md)
  The content of an alert for a forwarded Live Activity.
### Accessing the app’s icon
- [let sourceBundleIcon: AccessoryLiveActivity.IconFile?](accessoryliveactivity/sourcebundleicon.md)
  The icon of the app that initiated the Live Activity.
- [AccessoryLiveActivity.IconFile](accessoryliveactivity/iconfile.md)
  An on-demand reference to the app icon of the app that started the Live Activity.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/accessoryliveactivity)*
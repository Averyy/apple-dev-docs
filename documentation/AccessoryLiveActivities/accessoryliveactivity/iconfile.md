# AccessoryLiveActivity.IconFile

**Framework**: Accessory Live Activities  
**Kind**: struct  
**Role**: Structure

An on-demand reference to the app icon of the app that started the Live Activity.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
struct IconFile
```

#### Overview

The system loads the app icon file asynchronously using the [`url`](./iconfile/url.md).

## Topics

### Accessing file data
- [var url: URL](./iconfile/url.md)
  A URL that locates the icon file’s data.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the app’s icon
- [let sourceBundleIcon: AccessoryLiveActivity.IconFile?](./sourcebundleicon.md)
  The icon of the app that initiated the Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/accessoryliveactivity/iconfile)*
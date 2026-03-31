# AccessoryLiveActivity.IconFile

**Framework**: Accessory Live Activities  
**Kind**: struct

An on-demand reference to the app icon of the app that started the Live Activity.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
struct IconFile
```

#### Overview

The system loads the app icon file asynchronously using the [`url`](accessoryliveactivity/iconfile/url.md).

## Topics

### Accessing file data
- [var url: URL](accessoryliveactivity/iconfile/url.md)
  A URL that locates the icon file’s data.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let sourceBundleIcon: AccessoryLiveActivity.IconFile?](accessoryliveactivity/sourcebundleicon.md)
  The icon of the app that initiated the Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/accessoryliveactivity/iconfile)*
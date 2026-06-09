# requestedMountOptions

**Framework**: FSKit  
**Kind**: property

A property that allows the file system to request for specific mount options from FSKit.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional var requestedMountOptions: FSVolume.MountOptions { get }
```

#### Discussion

FSKit reads this value after the volume replies to the [`mount(options:replyHandler:)`](fsvolume/handler/mount(options:replyhandler:).md) call. Changing the returned value during the runtime of the volume has no effect.

## See Also

- [FSVolume.MountOptions](fsvolume/mountoptions.md)
  Mount options to be requested from FSKit using the `requestedMountOptions` property.
- [var enableOpenUnlinkEmulation: Bool](fsvolume/handler/enableopenunlinkemulation.md)
  A property that allows the file system to use open-unlink emulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/requestedmountoptions)*
# requestedMountOptions

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A property that allows the file system to request for specific mount options from FSKit.

**Availability**:
- macOS 26.4+

## Declaration

```swift
optional var requestedMountOptions: FSVolume.MountOptions { get }
```

```objc
@property (readonly) FSMountOptions requestedMountOptions;
```

#### Discussion

FSKit reads this value after the volume replies to the `mount(options:)` call. Changing the returned value during the runtime of the volume has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/commonoperations/requestedmountoptions)*
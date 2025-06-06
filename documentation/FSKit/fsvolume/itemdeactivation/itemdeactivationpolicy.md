# itemDeactivationPolicy

**Framework**: FSKit  
**Kind**: property  
**Required**: Yes

A property that tells FSKit to which types of items the deactivation applies, if any.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var itemDeactivationPolicy: FSVolume.ItemDeactivationOptions { get }
```

#### Discussion

FSKit reads this value after the file system replies to the `loadResource` message. Changing the returned value during the runtime of the volume has no effect.

## See Also

- [FSVolume.ItemDeactivationOptions](fsvolume/itemdeactivationoptions.md)
  Options to specify the item deactivation policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivation/itemdeactivationpolicy)*
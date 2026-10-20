# itemDeactivationPolicy

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A property that tells FSKit to which types of items the deactivation applies, if any.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
var itemDeactivationPolicy: FSVolume.ItemDeactivationOptions { get }
```

```objc
@property (readonly) FSItemDeactivationOptions itemDeactivationPolicy;
```

#### Discussion

FSKit reads this value after the file system replies to the `loadResource` message. Changing the returned value during the runtime of the volume has no effect.

## See Also

### Setting deactivation policy
- [FSVolume.ItemDeactivationOptions](../itemdeactivationoptions.md)
  Options to specify the item deactivation policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivation/itemdeactivationpolicy)*
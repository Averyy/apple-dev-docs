# ColorSyncProfileCopyData(_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Copies the flattened data from a profile.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func ColorSyncProfileCopyData(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFData>!
```

```c
extern CFDataRefColorSyncProfileCopyData(ColorSyncProfileRef prof, CFErrorRef*error);
```

#### Return Value

The profile data on success, or `NULL` in case of failure.

## Parameters

- `prof`: The profile to copy the flattened data from.
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

### Embedding and extracting profiles
- [func ColorSyncProfileCreate(CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreate%28_,_%29.md)
  Creates a profile from ICC profile data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecopydata(_:_:))*
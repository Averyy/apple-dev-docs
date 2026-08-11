# ColorSyncProfileCreate(_:_:)

**Framework**: ColorSync  
**Kind**: func

Creates a profile from ICC profile data.

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
func ColorSyncProfileCreate(_ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?
```

#### Return Value

A new profile, or `NULL` in case of failure.

## Parameters

- `data`: The ICC profile data.
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

- [func ColorSyncProfileCopyData(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFData>!](colorsyncprofilecopydata(_:_:).md)
  Copies the flattened data from a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreate(_:_:))*
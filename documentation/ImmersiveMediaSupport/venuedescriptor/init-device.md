# init(device:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an empty `VenueDescriptor`, useful when creating a new `VenueDescriptor` in code (other than loading from an AIME file).

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(device: (any MTLDevice)? = nil)
```

## See Also

- [convenience init(aimeURL: URL, device: (any MTLDevice)?) async throws](venuedescriptor/init(aimeurl:device:).md)
  Initializes a `VenueDescriptor` instance from an AIME file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/init(device:))*
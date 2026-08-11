# ColorSyncAPIVersion()

**Framework**: ColorSync  
**Kind**: func

Returns the version of the ColorSync API.

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
func ColorSyncAPIVersion() -> UInt32
```

#### Return Value

The API version as a binary-coded decimal `uint32_t`. From most to least significant byte, the value encodes the major OS version, minor OS version, patch version, and API version — that is, `(major << 24) | (minor << 16) | (dot << 8) | (apiVersion & 0xFF)`.

## See Also

- [var COLORSYNC_API_VERSION: Int](colorsync_api_version.md)
- [var icVersion4Number: Int](icversion4number.md)
- [var icVersion4Point4Number: Int](icversion4point4number.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncapiversion())*
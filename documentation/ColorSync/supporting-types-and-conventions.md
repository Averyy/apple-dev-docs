# Supporting types and conventions

**Framework**: ColorSync

Reference the signatures and conventions that support the color-management APIs.

#### Overview

These symbols support the main color-management tasks rather than being entry points themselves. You use them while working with profiles: to identify a tag inside a profile, or to check the framework version. The header and availability macros are compiler-level implementation details rather than callable API.

## Topics

### Identifying profile tags and signatures
- [Profile tags and signatures](profile-tags-and-signatures.md)
  Identify the four-character signatures that describe an ICC profile’s tags, class, and color space.
### Versioning
- [var COLORSYNC_API_VERSION: Int](colorsync_api_version.md)
- [func ColorSyncAPIVersion() -> UInt32](colorsyncapiversion().md)
- [var icVersion4Number: Int](icversion4number.md)
- [var icVersion4Point4Number: Int](icversion4point4number.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/supporting-types-and-conventions)*
# Supporting types and conventions

**Framework**: ColorSync  
**Role**: API Collection

Reference the signatures and conventions that support the color-management APIs.

#### Overview

These symbols support the main color-management tasks rather than being entry points themselves. You use them while working with profiles: to identify a tag inside a profile, or to check the framework version. The header and availability macros are compiler-level implementation details rather than callable API.

## Topics

### Identifying profile tags and signatures
- [Profile tags and signatures](./profile-tags-and-signatures.md)
  Identify the four-character signatures that describe an ICC profile’s tags, class, and color space.
### Versioning
- [var COLORSYNC_API_VERSION: Int](./colorsync_api_version.md)
- [func ColorSyncAPIVersion() -> UInt32](./colorsyncapiversion%28%29.md)
  Returns the version of the ColorSync API.
- [var icVersion4Number: Int](./icversion4number.md)
- [var icVersion4Point4Number: Int](./icversion4point4number.md)
### Annotating availability
- [CS_AVAILABLE_DESKTOP](./cs_available_desktop.md)
- [CS_AVAILABLE_STARTING](./cs_available_starting.md)
- [CS_AVAILABLE_STARTING1](./cs_available_starting1.md)
- [CS_AVAILABLE_STARTING2](./cs_available_starting2.md)
- [CS_AVAILABLE_STARTING_IOS](./cs_available_starting_ios.md)
- [CS_UNAVAILABLE_DESKTOP](./cs_unavailable_desktop.md)
- [CS_UNAVAILABLE_EMBEDDED](./cs_unavailable_embedded.md)
- [GET_CS_AVAIL_MACRO](./get_cs_avail_macro.md)
### Annotating deprecation
- [CS_AVAILABLE_BUT_DEPRECATED](./cs_available_but_deprecated.md)
- [CS_AVAILABLE_BUT_DEPRECATED1](./cs_available_but_deprecated1.md)
- [CS_AVAILABLE_BUT_DEPRECATED2](./cs_available_but_deprecated2.md)
- [CS_AVAILABLE_BUT_DEPRECATED3](./cs_available_but_deprecated3.md)
- [CS_AVAILABLE_BUT_DEPRECATED4](./cs_available_but_deprecated4.md)
- [CS_AVAILABLE_BUT_DEPRECATED5](./cs_available_but_deprecated5.md)
- [GET_CS_AVAIL_BUT_DEPR_MACRO](./get_cs_avail_but_depr_macro.md)
### Controlling symbol visibility
- [CSEXPORT](./csexport.md)
- [CSEXTERN](./csextern.md)
- [CSEXTERN_DESKTOP](./csextern_desktop.md)
- [CSLOCAL](./cslocal.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/supporting-types-and-conventions)*
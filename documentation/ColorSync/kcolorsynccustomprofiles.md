# kColorSyncCustomProfiles

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

A key whose value is a `CFDictionary` describing the device’s custom profiles.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncCustomProfiles: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncCustomProfiles;
```

## See Also

### Accessing custom and factory profiles
- [var kColorSyncFactoryProfiles: Unmanaged<CFString>!](./kcolorsyncfactoryprofiles.md)
  A key whose value is a `CFDictionary` describing the device’s factory profiles.
- [var kColorSyncDoNotSubstituteProfiles: Unmanaged<CFString>!](./kcolorsyncdonotsubstituteprofiles.md)
  An option that, when set to `kCFBooleanTrue`, skips substituting a matching system-provided profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsynccustomprofiles)*
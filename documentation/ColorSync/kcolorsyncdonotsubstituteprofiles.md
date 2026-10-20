# kColorSyncDoNotSubstituteProfiles

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

An option that, when set to `kCFBooleanTrue`, skips substituting a matching system-provided profile.

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
var kColorSyncDoNotSubstituteProfiles: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncDoNotSubstituteProfiles;
```

## See Also

### Accessing custom and factory profiles
- [var kColorSyncCustomProfiles: Unmanaged<CFString>!](./kcolorsynccustomprofiles.md)
  A key whose value is a `CFDictionary` describing the device’s custom profiles.
- [var kColorSyncFactoryProfiles: Unmanaged<CFString>!](./kcolorsyncfactoryprofiles.md)
  A key whose value is a `CFDictionary` describing the device’s factory profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncdonotsubstituteprofiles)*
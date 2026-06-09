# spatialExtensionDescription

**Framework**: AudioAccessoryKit  
**Kind**: property

The spatial audio component description.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var spatialExtensionDescription: AudioComponentDescription?
```

#### Discussion

Use this to help identify spatial audio rendering extension Only applicable when `.audioSpatialization` capability is enabled Example AudioComponentDescription(componentType: 0xaaf, componentSubType: 0xc0f, componentManufacturer: 0xb05e, componentFlags: 0, componentFlagsMask: 0)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct/spatialextensiondescription)*
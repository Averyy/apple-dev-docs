# init(contentsOf:)

**Framework**: Core Haptics  
**Kind**: init

Creates a haptic pattern with the contents of an AHAP file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(contentsOf ahapURL: URL) throws
```

## Parameters

- `ahapURL`: A URL to an AHAP file that describes a pattern.

## See Also

- [init(events: [CHHapticEvent], parameterCurves: [CHHapticParameterCurve]) throws](chhapticpattern/init(events:parametercurves:).md)
  Constructs a haptic pattern from a series of events and parameter curves.
- [init(events: [CHHapticEvent], parameters: [CHHapticDynamicParameter]) throws](chhapticpattern/init(events:parameters:).md)
  Constructs a haptic pattern from a series of events and parameters.
- [init(dictionary: [CHHapticPattern.Key : Any]) throws](chhapticpattern/init(dictionary:).md)
  Creates a haptic pattern from a property list dictionary.
- [CHHapticPattern.Key](chhapticpattern/key.md)
  Constants that define the keys you use to create a haptic pattern dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpattern/init(contentsof:))*
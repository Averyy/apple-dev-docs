# init(events:parameters:)

**Framework**: Core Haptics  
**Kind**: init

Constructs a haptic pattern from a series of events and parameters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(events: [CHHapticEvent], parameters: [CHHapticDynamicParameter]) throws
```

## Parameters

- `events`: An array of events that make up the haptic pattern.
- `parameters`: An array of dynamic parameters that define how the haptic pattern’s parameters change over time.

## See Also

- [init(contentsOf: URL) throws](chhapticpattern/init(contentsof:).md)
  Creates a haptic pattern with the contents of an AHAP file.
- [init(events: [CHHapticEvent], parameterCurves: [CHHapticParameterCurve]) throws](chhapticpattern/init(events:parametercurves:).md)
  Constructs a haptic pattern from a series of events and parameter curves.
- [init(dictionary: [CHHapticPattern.Key : Any]) throws](chhapticpattern/init(dictionary:).md)
  Creates a haptic pattern from a property list dictionary.
- [CHHapticPattern.Key](chhapticpattern/key.md)
  Constants that define the keys you use to create a haptic pattern dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpattern/init(events:parameters:))*
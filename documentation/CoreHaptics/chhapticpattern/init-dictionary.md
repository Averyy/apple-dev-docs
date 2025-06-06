# init(dictionary:)

**Framework**: Core Haptics  
**Kind**: init

Creates a haptic pattern from a property list dictionary.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(dictionary patternDict: [CHHapticPattern.Key : Any]) throws
```

## Parameters

- `patternDict`: A dictionary that defines the haptic pattern and its parameters.

## See Also

- [init(contentsOf: URL) throws](chhapticpattern/init(contentsof:).md)
  Creates a haptic pattern with the contents of an AHAP file.
- [init(events: [CHHapticEvent], parameterCurves: [CHHapticParameterCurve]) throws](chhapticpattern/init(events:parametercurves:).md)
  Constructs a haptic pattern from a series of events and parameter curves.
- [init(events: [CHHapticEvent], parameters: [CHHapticDynamicParameter]) throws](chhapticpattern/init(events:parameters:).md)
  Constructs a haptic pattern from a series of events and parameters.
- [CHHapticPattern.Key](chhapticpattern/key.md)
  Constants that define the keys you use to create a haptic pattern dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpattern/init(dictionary:))*
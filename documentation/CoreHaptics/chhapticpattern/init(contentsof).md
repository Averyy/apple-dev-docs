# init(contentsOf:)

**Framework**: Core Haptics  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithContentsOfURL:(NSURL *) ahapURL error:(NSError **) outError;
```

## Parameters

- `ahapURL`: A URL to an AHAP file that describes a pattern.

## See Also

### Creating a Haptic Pattern
- [init(events: [CHHapticEvent], parameterCurves: [CHHapticParameterCurve]) throws](./init%28events,parametercurves%29.md)
  Constructs a haptic pattern from a series of events and parameter curves.
- [init(events: [CHHapticEvent], parameters: [CHHapticDynamicParameter]) throws](./init%28events,parameters%29.md)
  Constructs a haptic pattern from a series of events and parameters.
- [init(dictionary: [CHHapticPattern.Key : Any]) throws](./init%28dictionary%29.md)
  Creates a haptic pattern from a property list dictionary.
- [CHHapticPattern.Key](./key.md)
  Constants that define the keys you use to create a haptic pattern dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpattern/init(contentsof:))*
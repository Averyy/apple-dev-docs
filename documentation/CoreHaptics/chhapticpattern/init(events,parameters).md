# init(events:parameters:)

**Framework**: Core Haptics  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithEvents:(NSArray<CHHapticEvent *> *) events parameters:(NSArray<CHHapticDynamicParameter *> *) parameters error:(NSError **) outError;
```

## Parameters

- `events`: An array of events that make up the haptic pattern.
- `parameters`: An array of dynamic parameters that define how the haptic pattern’s parameters change over time.

## See Also

### Creating a Haptic Pattern
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
  Creates a haptic pattern with the contents of an AHAP file.
- [init(events: [CHHapticEvent], parameterCurves: [CHHapticParameterCurve]) throws](./init%28events,parametercurves%29.md)
  Constructs a haptic pattern from a series of events and parameter curves.
- [init(dictionary: [CHHapticPattern.Key : Any]) throws](./init%28dictionary%29.md)
  Creates a haptic pattern from a property list dictionary.
- [CHHapticPattern.Key](./key.md)
  Constants that define the keys you use to create a haptic pattern dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpattern/init(events:parameters:))*
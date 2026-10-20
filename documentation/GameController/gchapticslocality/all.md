# all

**Framework**: Game Controller  
**Kind**: property  
**Role**: Type Property

All locations of haptics actuators on a game controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let all: GCHapticsLocality
```

```c
extern GCHapticsLocality const GCHapticsLocalityAll;
```

#### Discussion

Controllers must support this location, and it can be the same as [`default`](./default.md).

## See Also

### Localities
- [static let `default`: GCHapticsLocality](./default.md)
  The default location of a haptics actuator on a game controller.
- [static let handles: GCHapticsLocality](./handles.md)
  All handles on a game controller.
- [static let leftHandle: GCHapticsLocality](./lefthandle.md)
  The left handle on a game controller.
- [static let rightHandle: GCHapticsLocality](./righthandle.md)
  The right handle on a game controller.
- [static let triggers: GCHapticsLocality](./triggers.md)
  All triggers on a game controller.
- [static let leftTrigger: GCHapticsLocality](./lefttrigger.md)
  The left trigger on a game controller.
- [static let rightTrigger: GCHapticsLocality](./righttrigger.md)
  The right trigger on a game controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gchapticslocality/all)*
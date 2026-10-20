# supportedLocalities

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The locations of haptic actuators on the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var supportedLocalities: Set<GCHapticsLocality> { get }
```

```objc
@property (copy, readonly) NSSet<NSString *> * supportedLocalities;
```

## See Also

### Getting the localities
- [struct GCHapticsLocality](../gchapticslocality.md)
  The location of one or more haptics actuators on a game controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicehaptics/supportedlocalities)*
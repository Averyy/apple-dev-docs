# init(pressureBehavior:)

**Framework**: AppKit  
**Kind**: init

Initializes a pressure configuration object with a specified pressure behavior.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
init(pressureBehavior: NSEvent.PressureBehavior)
```

#### Return Value

A new pressure configuration object of type `NSPressureConfiguration` that describes how pressure events behave and progress.

#### Discussion

The initialized pressure configuration object is used to change the behavior and progression of the trackpad when responding to a mouse drag or pressure event sequence.

## Parameters

- `pressureBehavior`: An   value that describes the behavior and progression for responding to pressure events.

## See Also

- [NSEvent.PressureBehavior](nsevent/pressurebehavior-swift.enum.md)
  These constants describe the behavior and progression of a pressure gesture.
- [func set()](nspressureconfiguration/set.md)
  Changes the pressure configuration of the trackpad to the initialized pressure configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressureconfiguration/init(pressurebehavior:))*
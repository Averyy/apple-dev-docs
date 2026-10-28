# unmapped

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The live input of a controller without any system-level remapping of the controls.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var unmapped: GCControllerLiveInput? { get }
```

```objc
@property (readonly, nullable) GCControllerLiveInput * unmappedInput;
```

## Discussion

Players should use the system game controller settings to remap controls. If you implement your own controller remapping feature, use this property to access the controller’s physical input without remapping applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerliveinput/unmapped)*
# allTouchpads

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The touchpads in the profile.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var allTouchpads: Set<GCControllerTouchpad> { get }
```

```objc
@property (nonatomic, strong, readonly) NSSet<GCControllerTouchpad *> * allTouchpads;
```

## See Also

### Getting elements by type
- [var allElements: Set<GCControllerElement>](./allelements.md)
  The elements in the profile.
- [var allButtons: Set<GCControllerButtonInput>](./allbuttons.md)
  The buttons in the profile.
- [var allAxes: Set<GCControllerAxisInput>](./allaxes.md)
  The axes in the profile.
- [var allDpads: Set<GCControllerDirectionPad>](./alldpads.md)
  The directional pads in the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/alltouchpads)*
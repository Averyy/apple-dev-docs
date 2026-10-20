# valueStep

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The value of the slider moves towards the associated value for the accessory with by a delta of the slider’s `altIncrementValue`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
@NSCopying
class var valueStep: NSSliderAccessoryBehavior { get }
```

```objc
@property (class, copy, readonly) NSSliderAccessoryBehavior * valueStepBehavior;
```

## See Also

### Type Properties
- [class var automatic: NSSliderAccessoryBehavior](./automatic.md)
  The behavior is automatically picked to be the system standard, given the slider’s current context.
- [class var valueReset: NSSliderAccessoryBehavior](./valuereset.md)
  The value of the slider is reset to the associated value for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessorybehavior/valuestep)*
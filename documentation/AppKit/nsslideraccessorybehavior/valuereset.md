# valueReset

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The value of the slider is reset to the associated value for the accessory.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
@NSCopying
class var valueReset: NSSliderAccessoryBehavior { get }
```

```objc
@property (class, copy, readonly) NSSliderAccessoryBehavior * valueResetBehavior;
```

## See Also

### Type Properties
- [class var automatic: NSSliderAccessoryBehavior](./automatic.md)
  The behavior is automatically picked to be the system standard, given the slider’s current context.
- [class var valueStep: NSSliderAccessoryBehavior](./valuestep.md)
  The value of the slider moves towards the associated value for the accessory with by a delta of the slider’s `altIncrementValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessorybehavior/valuereset)*
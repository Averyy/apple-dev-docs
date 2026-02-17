# automatic

**Framework**: AppKit  
**Kind**: property

The behavior is automatically picked to be the system standard, given the slider’s current context.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
@NSCopying
class var automatic: NSSliderAccessoryBehavior { get }
```

#### Discussion

For example, NSTouchBarItems have `.valueStep` behavior.

## See Also

- [class var valueReset: NSSliderAccessoryBehavior](nsslideraccessorybehavior/valuereset.md)
  The value of the slider is reset to the associated value for the accessory.
- [class var valueStep: NSSliderAccessoryBehavior](nsslideraccessorybehavior/valuestep.md)
  The value of the slider moves towards the associated value for the accessory with by a delta of the slider’s `altIncrementValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessorybehavior/automatic)*
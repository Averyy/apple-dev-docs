# switchedOnContents

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The contents for the switch when it is switched on.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var switchedOnContents: TCControlContents? { get set }
```

```objc
@property (nonatomic, strong, nullable) TCControlContents * switchedOnContents;
```

## Discussion

This value can be `nil`.

## See Also

### Inspecting the switch
- [var contents: TCControlContents?](./contents.md)
  The contents for the switch in its normal state.
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var isSwitchedOn: Bool](./isswitchedon.md)
  A Boolean value that indicates whether the switch is currently switched on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcswitch/switchedoncontents)*
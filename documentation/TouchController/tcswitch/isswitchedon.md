# isSwitchedOn

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the switch is currently switched on.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var isSwitchedOn: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isSwitchedOn) BOOL switchedOn;
```

## See Also

### Inspecting the switch
- [var contents: TCControlContents?](./contents.md)
  The contents for the switch in its normal state.
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The time it takes for a highlight to fade away, in seconds.
- [var switchedOnContents: TCControlContents?](./switchedoncontents.md)
  The contents for the switch when it is switched on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcswitch/isswitchedon)*
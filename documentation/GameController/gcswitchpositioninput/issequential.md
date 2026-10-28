# isSequential

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the position change is sequential.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var isSequential: Bool { get }
```

```objc
@property (readonly, getter=isSequential) BOOL sequential;
```

## Discussion

A sequential gear shift requires the user to move through the gears in sequence.

## See Also

### Getting the characteristics
- [var positionRange: NSRange](./positionrange.md)
  The range of possible values for the switch.
- [var canWrap: Bool](./canwrap.md)
  A Boolean value that indicates whether the position value wraps when it reaches the range’s minimum or maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput/issequential)*
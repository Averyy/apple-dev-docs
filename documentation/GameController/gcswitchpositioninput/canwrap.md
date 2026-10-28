# canWrap

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the position value wraps when it reaches the range’s minimum or maximum value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var canWrap: Bool { get }
```

```objc
@property (readonly) BOOL canWrap;
```

## Discussion

For non-sequential switches, this property is always [`true`](../../Swift/true.md).

## See Also

### Getting the characteristics
- [var positionRange: NSRange](./positionrange.md)
  The range of possible values for the switch.
- [var isSequential: Bool](./issequential.md)
  A Boolean value that indicates whether the position change is sequential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput/canwrap)*
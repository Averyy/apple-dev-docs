# positionRange

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The range of possible values for the switch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var positionRange: NSRange { get }
```

```objc
@property (readonly) NSRange positionRange;
```

## See Also

### Getting the characteristics
- [var isSequential: Bool](./issequential.md)
  A Boolean value that indicates whether the position change is sequential.
- [var canWrap: Bool](./canwrap.md)
  A Boolean value that indicates whether the position value wraps when it reaches the range’s minimum or maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchpositioninput/positionrange)*
# isAnalog

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the input provides analog values.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var isAnalog: Bool { get }
```

```objc
@property (readonly, getter=isAnalog) BOOL analog;
```

#### Discussion

This property is [`true`](../../Swift/true.md) for most axis inputs.

## See Also

### Getting the characteristics
- [var canWrap: Bool](./canwrap.md)
  A Boolean value that indicates whether the value wraps when it reaches the range’s minimum or maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxis2dinput/isanalog)*
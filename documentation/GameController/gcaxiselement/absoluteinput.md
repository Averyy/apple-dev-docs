# absoluteInput

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An input object that provides absolute axis values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var absoluteInput: (any GCAxisInput)? { get }
```

```objc
@property (readonly, nullable) id<GCAxisInput> absoluteInput;
```

## See Also

### Getting the inputs
- [var relativeInput: any GCRelativeInput](./relativeinput.md)
  An input object that provides relative axis values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxiselement/absoluteinput)*
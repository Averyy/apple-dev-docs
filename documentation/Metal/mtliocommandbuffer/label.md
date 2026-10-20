# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An optional name for the input/output command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

```objc
@property (atomic, copy, nullable) NSString * label;
```

## See Also

### Debugging a command buffer
- [func pushDebugGroup(String)](./pushdebuggroup%28_%29.md)
  Sets the current name for this input/output command encoder by adding it to the top of the debug name stack.
- [func popDebugGroup()](./popdebuggroup%28%29.md)
  Restores the previous name for this input/output command encoder by removing the top item of the debug name stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/label)*
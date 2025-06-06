# value

**Framework**: ClassKit  
**Kind**: property

The value that the binary activity item takes.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var value: Bool { get set }
```

#### Discussion

Interpret this value according to the binary activity item’s [`valueType`](clsbinaryitem/valuetype.md). For example, if the value type is set to [`CLSBinaryValueType.passFail`](clsbinaryvaluetype/passfail.md), then false means fail, and true means pass.

## See Also

- [var valueType: CLSBinaryValueType](clsbinaryitem/valuetype.md)
  The kind of outcome that the binary activity item represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsbinaryitem/value)*
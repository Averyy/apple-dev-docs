# valueType

**Framework**: ClassKit  
**Kind**: property

The kind of outcome that the binary activity item represents.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var valueType: CLSBinaryValueType { get }
```

#### Discussion

Use this property to indicate how to present the binary result stored in the [`value`](clsbinaryitem/value.md) property to a teacher. For example, you might use a binary item to indicate whether a student passed a quiz, in which case you set [`valueType`](clsbinaryitem/valuetype.md) to [`CLSBinaryValueType.passFail`](clsbinaryvaluetype/passfail.md). If you use another binary item to indicate whether a student used a hint while taking the quiz, set its [`valueType`](clsbinaryitem/valuetype.md) to [`CLSBinaryValueType.yesNo`](clsbinaryvaluetype/yesno.md). For a complete list of possible values, see the [`CLSBinaryValueType`](clsbinaryvaluetype.md) enumeration.

## See Also

- [var value: Bool](clsbinaryitem/value.md)
  The value that the binary activity item takes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsbinaryitem/valuetype)*
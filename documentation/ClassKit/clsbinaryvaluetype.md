# CLSBinaryValueType

**Framework**: ClassKit  
**Kind**: enum  
**Role**: Enumeration

The kinds of outcomes that a binary activity item can represent.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum CLSBinaryValueType
```

```c
enum CLSBinaryValueType : NSInteger;
```

## Topics

### Value Types
- [CLSBinaryValueType.passFail](./clsbinaryvaluetype/passfail.md)
  Pass or fail.
- [CLSBinaryValueType.trueFalse](./clsbinaryvaluetype/truefalse.md)
  True or false.
- [CLSBinaryValueType.yesNo](./clsbinaryvaluetype/yesno.md)
  Yes or no.
- [CLSBinaryValueType.correctIncorrect](./clsbinaryvaluetype/correctincorrect.md)
  Correct or incorrect.
### Initializers
- [init?(rawValue: Int)](./clsbinaryvaluetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Binary Activity Items
- [init(identifier: String, title: String, type: CLSBinaryValueType)](./clsbinaryitem/init%28identifier,title,type%29.md)
  Initializes a new binary activity item of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsbinaryvaluetype)*
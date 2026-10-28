# value

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) BOOL value;
```

## Discussion

Interpret this value according to the binary activity item’s [`valueType`](./valuetype.md). For example, if the value type is set to [`CLSBinaryValueType.passFail`](../clsbinaryvaluetype/passfail.md), then false means fail, and true means pass.

## See Also

### Managing the Value
- [var valueType: CLSBinaryValueType](./valuetype.md)
  The kind of outcome that the binary activity item represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsbinaryitem/value)*
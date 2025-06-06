# CTParagraphStyleSetting

**Framework**: Core Text  
**Kind**: struct

This structure is used to alter the paragraph style.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CTParagraphStyleSetting
```

## Topics

### Initializers
- [init(spec: CTParagraphStyleSpecifier, valueSize: Int, value: UnsafeRawPointer)](ctparagraphstylesetting/init(spec:valuesize:value:).md)
### Instance Properties
- [var spec: CTParagraphStyleSpecifier](ctparagraphstylesetting/spec.md)
  The specifier of the setting. See [`CTParagraphStyleSpecifier`](ctparagraphstylespecifier.md) for possible values.
- [var value: UnsafeRawPointer](ctparagraphstylesetting/value.md)
  A reference to the value of the setting specified by the `spec` field. The value must be in the proper range for the `spec` value and at least as large as the size specified in `valueSize`.
- [var valueSize: Int](ctparagraphstylesetting/valuesize.md)
  The size of the value pointed to by the `value` field. This value must match the size of the value required by the `CTParagraphStyleSpecifier` set in the `spec` field.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctparagraphstylesetting)*
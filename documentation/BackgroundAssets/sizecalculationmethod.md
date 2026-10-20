# SizeCalculationMethod

**Framework**: Background Assets  
**Kind**: enum  
**Role**: Enumeration

Methods for calculating a file’s size.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```swift
enum SizeCalculationMethod
```

```c
enum BASizeCalculationMethod : NSInteger;
```

## Topics

### Enumeration Cases
- [SizeCalculationMethod.allocated](./sizecalculationmethod/allocated.md)
  A calculation method that counts the number of bytes that the file system allocated for a file.
- [SizeCalculationMethod.logical](./sizecalculationmethod/logical.md)
  A calculation method that counts the number of bytes in a file.
### Initializers
- [init?(rawValue: Int)](./sizecalculationmethod/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/sizecalculationmethod)*
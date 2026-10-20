# NSSpecifierTest.TestComparisonOperation

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These are passed to  [`init(objectSpecifier:comparisonOperator:test:)`](./init%28objectspecifier,comparisonoperator,test%29.md) to specify the comparison operator.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum TestComparisonOperation
```

```c
enum NSTestComparisonOperation : NSUInteger;
```

## Topics

### Constants
- [NSSpecifierTest.TestComparisonOperation.equal](./testcomparisonoperation/equal.md)
  Binary comparison operator that results in true if the two objects are equal.
- [NSSpecifierTest.TestComparisonOperation.lessThanOrEqual](./testcomparisonoperation/lessthanorequal.md)
  Binary comparison operator that results in true if the value of the test object is equal to or less than the value of the other object.
- [NSSpecifierTest.TestComparisonOperation.lessThan](./testcomparisonoperation/lessthan.md)
  Binary comparison operator that results in true if the value of the test object is less than the value of the other object.
- [NSSpecifierTest.TestComparisonOperation.greaterThanOrEqual](./testcomparisonoperation/greaterthanorequal.md)
  Binary comparison operator that results in true if the value of the test object is greater than or equal to the value of the other object.
- [NSSpecifierTest.TestComparisonOperation.greaterThan](./testcomparisonoperation/greaterthan.md)
  Binary comparison operator that results in true if the value of the test object is greater than the value of the other object.
- [NSSpecifierTest.TestComparisonOperation.beginsWith](./testcomparisonoperation/beginswith.md)
  Binary containment operator that results in true if the test object is a list or string that matches the beginning of the other object (which is also a list or string).
- [NSSpecifierTest.TestComparisonOperation.endsWith](./testcomparisonoperation/endswith.md)
  Binary containment operator that results in true if the test object is a list or string that matches the end of the other object (which is also a list or string).
- [NSSpecifierTest.TestComparisonOperation.contains](./testcomparisonoperation/contains.md)
  Binary containment operator that results in true if the test object is a list or string that matches the other object (which is also a list or string) at any location.
### Initializers
- [init?(rawValue: UInt)](./testcomparisonoperation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspecifiertest/testcomparisonoperation)*
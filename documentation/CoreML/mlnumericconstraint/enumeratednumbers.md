# enumeratedNumbers

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A set of the numbers allowed in this constraint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var enumeratedNumbers: Set<NSNumber>? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSSet<NSNumber *> * enumeratedNumbers;
```

## See Also

### Numeric Constraints
- [var minNumber: NSNumber](./minnumber.md)
  The smallest numerical value allowed by this constraint.
- [var maxNumber: NSNumber](./maxnumber.md)
  The largest numerical value allowed by this constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlnumericconstraint/enumeratednumbers)*
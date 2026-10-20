# value

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The category value for this sample.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var value: Int { get }
```

```objc
@property (readonly) NSInteger value;
```

#### Discussion

This value must come from the appropriate category value enumeration. Each category type uses its own enumeration. For more information, see Category Type Identifiers in [HealthKit Constants](../healthkit-constants.md).

## See Also

### Getting Property Data
- [var categoryType: HKCategoryType](./categorytype.md)
  The category type for this sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorysample/value)*
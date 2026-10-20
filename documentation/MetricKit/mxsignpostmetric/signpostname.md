# signpostName

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The developer-specified name of the custom metric represented by the object.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`signpostName`](../signpostintervalmetric/signpostname.md) instead.

## Declaration

```swift
var signpostName: String { get }
```

```objc
@property (strong, readonly, nonnull) NSString * signpostName;
```

## See Also

### Reading data about the custom metric
- [var signpostCategory: String](./signpostcategory.md)
  The developer-specified category of the custom metric represented by the object.
- [var totalCount: Int](./totalcount.md)
  The total number of occurrences of the captured custom metric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostmetric/signpostname)*
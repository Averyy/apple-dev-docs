# NSFeatureUnsupportedError

**Framework**: Foundation  
**Kind**: var

The feature isn’t supported, because the file system lacks the feature, or required libraries are missing, or other similar reasons.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var NSFeatureUnsupportedError: Int { get }
```

#### Discussion

For example, some volumes may not support a Trash folder, so these methods will report failure by returning [`false`](https://developer.apple.com/documentation/swift/false) or `nil` and an [`NSError`](nserror.md) with [`NSFeatureUnsupportedError`](nsfeatureunsupportederror-swift.var.md).

## See Also

- [var NSKeyValueValidationError: Int](nskeyvaluevalidationerror-swift.var.md)
  A key-value coding validation error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfeatureunsupportederror-swift.var)*
# stringRepresentation

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A string representation of the version.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var stringRepresentation: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * stringRepresentation;
```

## Discussion

The string representation uses the following format: `<major>.<minor>.<patch>`.

## See Also

### Accessing Version Data
- [var majorVersion: Int](./majorversion.md)
  The standard’s major version number.
- [var minorVersion: Int](./minorversion.md)
  The standard’s minor version number.
- [var patchVersion: Int](./patchversion.md)
  The standard’s patch version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirversion/stringrepresentation)*
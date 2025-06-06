# stringRepresentation

**Framework**: HealthKit  
**Kind**: property

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

#### Discussion

The string representation uses the following format: `<major>.<minor>.<patch>`.

## See Also

- [var majorVersion: Int](hkfhirversion/majorversion.md)
  The standard’s major version number.
- [var minorVersion: Int](hkfhirversion/minorversion.md)
  The standard’s minor version number.
- [var patchVersion: Int](hkfhirversion/patchversion.md)
  The standard’s patch version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirversion/stringrepresentation)*
# init(fromVersionString:)

**Framework**: HealthKit  
**Kind**: init

Creates an FHIR version object from a string representation of the version.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(fromVersionString versionString: String) throws
```

#### Discussion

The string must be in the following format: `<major>.<minor>.<patch>`.

## Parameters

- `versionString`: A string representing the version.

## See Also

- [class func primaryDSTU2() -> Self](hkfhirversion/primarydstu2.md)
  Returns the primary Second Draft Standard for Trial Use (DSTU2) version.
- [class func primaryR4() -> Self](hkfhirversion/primaryr4.md)
  Returns the primary Release 4 (R4) version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirversion/init(fromversionstring:))*
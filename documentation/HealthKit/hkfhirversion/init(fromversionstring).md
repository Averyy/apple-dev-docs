# init(fromVersionString:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) versionFromVersionString:(NSString *) versionString error:(NSError **) errorOut;
```

#### Discussion

The string must be in the following format: `<major>.<minor>.<patch>`.

## Parameters

- `versionString`: A string representing the version.

## See Also

### Creating Version Objects
- [class func primaryDSTU2() -> Self](./primarydstu2%28%29.md)
  Returns the primary Second Draft Standard for Trial Use (DSTU2) version.
- [class func primaryR4() -> Self](./primaryr4%28%29.md)
  Returns the primary Release 4 (R4) version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkfhirversion/init(fromversionstring:))*
# bundleIdentifier

**Framework**: SensorKit  
**Kind**: property

The bundle identifier of the app in use.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var bundleIdentifier: String? { get }
```

#### Discussion

The framework sets a value for this property only if the bundle identifier corresponds to an Apple app. Otherwise, you can correlate the app by using the [`reportApplicationIdentifier`](srdeviceusagereport/applicationusage/reportapplicationidentifier.md) property.

## See Also

- [var reportApplicationIdentifier: String](srdeviceusagereport/applicationusage/reportapplicationidentifier.md)
  A pseudonymn for a real application identifier.
- [var supplementalCategories: [SRSupplementalCategory]](srdeviceusagereport/applicationusage/supplementalcategories.md)
  Categories that provide more information about an app.
- [class SRSupplementalCategory](srsupplementalcategory.md)
  A more detailed category that provides additional context to the app category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier)*
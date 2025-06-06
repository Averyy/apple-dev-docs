# reportApplicationIdentifier

**Framework**: SensorKit  
**Kind**: property

A pseudonymn for a real application identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var reportApplicationIdentifier: String { get }
```

#### Discussion

The value of this property uniquely refers to a single app throughout the report without revealing the app’s true identity. For user privacy, the system assigns this property a pseudonymous string in cases where the [`bundleIdentifier`](srdeviceusagereport/applicationusage/bundleidentifier.md) is `nil`.

## See Also

- [var bundleIdentifier: String?](srdeviceusagereport/applicationusage/bundleidentifier.md)
  The bundle identifier of the app in use.
- [var supplementalCategories: [SRSupplementalCategory]](srdeviceusagereport/applicationusage/supplementalcategories.md)
  Categories that provide more information about an app.
- [class SRSupplementalCategory](srsupplementalcategory.md)
  A more detailed category that provides additional context to the app category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier)*
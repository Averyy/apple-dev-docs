# reportApplicationIdentifier

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

A pseudonymn for a real application identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var reportApplicationIdentifier: String { get }
```

```objc
@property (copy, readonly) NSString * reportApplicationIdentifier;
```

## Discussion

The value of this property uniquely refers to a single app throughout the report without revealing the app’s true identity. For user privacy, the system assigns this property a pseudonymous string in cases where the [`bundleIdentifier`](./bundleidentifier.md) is `nil`.

## See Also

### Identifying the App
- [var bundleIdentifier: String?](./bundleidentifier.md)
  The bundle identifier of the app in use.
- [var supplementalCategories: [SRSupplementalCategory]](./supplementalcategories.md)
  Categories that provide more information about an app.
- [class SRSupplementalCategory](../../srsupplementalcategory.md)
  A more detailed category that provides additional context to the app category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/reportapplicationidentifier)*
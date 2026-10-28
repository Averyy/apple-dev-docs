# bundleIdentifier

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The bundle identifier of the app in use.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var bundleIdentifier: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * bundleIdentifier;
```

## Discussion

The framework sets a value for this property only if the bundle identifier corresponds to an Apple app. Otherwise, you can correlate the app by using the [`reportApplicationIdentifier`](./reportapplicationidentifier.md) property.

## See Also

### Identifying the App
- [var reportApplicationIdentifier: String](./reportapplicationidentifier.md)
  A pseudonymn for a real application identifier.
- [var supplementalCategories: [SRSupplementalCategory]](./supplementalcategories.md)
  Categories that provide more information about an app.
- [class SRSupplementalCategory](../../srsupplementalcategory.md)
  A more detailed category that provides additional context to the app category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/bundleidentifier)*
# supplementalCategories

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

Categories that provide more information about an app.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var supplementalCategories: [SRSupplementalCategory] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<SRSupplementalCategory *> * supplementalCategories;
```

## See Also

### Identifying the App
- [var bundleIdentifier: String?](./bundleidentifier.md)
  The bundle identifier of the app in use.
- [var reportApplicationIdentifier: String](./reportapplicationidentifier.md)
  A pseudonymn for a real application identifier.
- [class SRSupplementalCategory](../../srsupplementalcategory.md)
  A more detailed category that provides additional context to the app category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/supplementalcategories)*
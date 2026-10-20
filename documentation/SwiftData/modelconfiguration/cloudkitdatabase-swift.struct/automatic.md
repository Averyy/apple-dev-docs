# automatic

**Framework**: SwiftData  
**Kind**: property  
**Role**: Type Property

Enables managed CloudKit sync using the primary ubiquity container from the app’s entitlements.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
static var automatic: ModelConfiguration.CloudKitDatabase { get }
```

## See Also

### Getting discovery options
- [static func `private`(String) -> ModelConfiguration.CloudKitDatabase](./private%28_%29.md)
  Enables managed CloudKit sync using the specified ubiquity container.
- [static var none: ModelConfiguration.CloudKitDatabase](./none.md)
  Disables managed CloudKit sync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct/automatic)*
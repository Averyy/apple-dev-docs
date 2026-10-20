# private(_:)

**Framework**: SwiftData  
**Kind**: method  
**Role**: Type Method

Enables managed CloudKit sync using the specified ubiquity container.

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
static func `private`(_ privateDBName: String) -> ModelConfiguration.CloudKitDatabase
```

## Parameters

- `privateDBName`: The identifier of the iCloud ubiquity container to use. You find these in the iCloud capabilities section of your Xcode project. For more information, see [Configuring iCloud services](../../../Xcode/configuring-icloud-services.md).

## See Also

### Getting discovery options
- [static var automatic: ModelConfiguration.CloudKitDatabase](./automatic.md)
  Enables managed CloudKit sync using the primary ubiquity container from the app’s entitlements.
- [static var none: ModelConfiguration.CloudKitDatabase](./none.md)
  Disables managed CloudKit sync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct/private(_:))*
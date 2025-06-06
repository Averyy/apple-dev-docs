# private(_:)

**Framework**: SwiftData  
**Kind**: method

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

- `privateDBName`: The identifier of the iCloud ubiquity container to use. You   find these in the iCloud capabilities section of your Xcode project. For more   information, see  .

## See Also

- [static var automatic: ModelConfiguration.CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.struct/automatic.md)
  Enables managed CloudKit sync using the primary ubiquity container from the app’s entitlements.
- [static var none: ModelConfiguration.CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.struct/none.md)
  Disables managed CloudKit sync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct/private(_:))*
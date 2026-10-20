# automatic

**Framework**: SwiftData  
**Kind**: property  
**Role**: Type Property

Tells SwiftData to use the app’s primary group container as the root location for the persistent storage.

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
static var automatic: ModelConfiguration.GroupContainer { get }
```

## See Also

### Getting discovery options
- [static func identifier(String) -> ModelConfiguration.GroupContainer](./identifier%28_%29.md)
  Tells SwiftData to use the specified group container as the root location for the app’s persistent storage.
- [static var none: ModelConfiguration.GroupContainer](./none.md)
  Prevents SwiftData from using a group container as the root location for the app’s persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/automatic)*
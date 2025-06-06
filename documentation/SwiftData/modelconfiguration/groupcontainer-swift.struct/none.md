# none

**Framework**: SwiftData  
**Kind**: property

Prevents SwiftData from using a group container as the root location for the app’s persistent storage.

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
static var none: ModelConfiguration.GroupContainer { get }
```

## See Also

- [static var automatic: ModelConfiguration.GroupContainer](modelconfiguration/groupcontainer-swift.struct/automatic.md)
  Tells SwiftData to use the app’s primary group container as the root location for the persistent storage.
- [static func identifier(String) -> ModelConfiguration.GroupContainer](modelconfiguration/groupcontainer-swift.struct/identifier(_:).md)
  Tells SwiftData to use the specified group container as the root location for the app’s persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/none)*
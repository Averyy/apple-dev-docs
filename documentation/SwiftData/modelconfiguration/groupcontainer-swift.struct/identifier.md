# identifier(_:)

**Framework**: SwiftData  
**Kind**: method

Tells SwiftData to use the specified group container as the root location for the app’s persistent storage.

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
static func identifier(_ groupName: String) -> ModelConfiguration.GroupContainer
```

## Parameters

- `groupName`: The identifier of the group container to use. You find these in   the App Groups capabilities section of your Xcode project. For more   information, see  .

## See Also

- [static var automatic: ModelConfiguration.GroupContainer](modelconfiguration/groupcontainer-swift.struct/automatic.md)
  Tells SwiftData to use the app’s primary group container as the root location for the persistent storage.
- [static var none: ModelConfiguration.GroupContainer](modelconfiguration/groupcontainer-swift.struct/none.md)
  Prevents SwiftData from using a group container as the root location for the app’s persistent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct/identifier(_:))*
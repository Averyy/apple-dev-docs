# TransferRepresentationVisibility

**Framework**: Core Transferable  
**Kind**: struct

The visibility levels that specify the kinds of apps and processes that can see an item in transit.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct TransferRepresentationVisibility
```

## Topics

### Specifying transfer visibility
- [static let all: TransferRepresentationVisibility](transferrepresentationvisibility/all.md)
  The visibility level that specifies that any app or process can access the item.
- [static let team: TransferRepresentationVisibility](transferrepresentationvisibility/team.md)
  The visibility level that specifies that the item is visible only to apps created by the current app’s development team.
- [static let group: TransferRepresentationVisibility](transferrepresentationvisibility/group.md)
  The visibility level that specifies that the item is visible only to macOS apps in the same App Group.
- [static let ownProcess: TransferRepresentationVisibility](transferrepresentationvisibility/ownprocess.md)
  The visibility level that specifies that the item is visible only within the app that’s the source of the item.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ProxyRepresentation](proxyrepresentation.md)
  A transfer representation that uses another type’s transfer representation as its own.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentationvisibility)*
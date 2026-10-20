# group

**Framework**: Core Transferable  
**Kind**: property  
**Role**: Type Property

The visibility level that specifies that the item is visible only to macOS apps in the same App Group.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static let group: TransferRepresentationVisibility
```

## See Also

### Specifying transfer visibility
- [static let all: TransferRepresentationVisibility](./all.md)
  The visibility level that specifies that any app or process can access the item.
- [static let team: TransferRepresentationVisibility](./team.md)
  The visibility level that specifies that the item is visible only to apps created by the current app’s development team.
- [static let ownProcess: TransferRepresentationVisibility](./ownprocess.md)
  The visibility level that specifies that the item is visible only within the app that’s the source of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/transferrepresentationvisibility/group)*
# NSBrowser.DropOperation

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The type used to specify the drop type of a drag-and-drop operation. See [`browser(_:validateDrop:proposedRow:column:dropOperation:)`](../nsbrowserdelegate/browser%28_,validatedrop,proposedrow,column,dropoperation%29.md) for more information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum DropOperation
```

```c
enum NSBrowserDropOperation : NSUInteger;
```

## Topics

### Constants
- [NSBrowser.DropOperation.on](./dropoperation/on.md)
- [NSBrowser.DropOperation.above](./dropoperation/above.md)
### Initializers
- [init?(rawValue: UInt)](./dropoperation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSBrowser.ColumnResizingType](./columnresizingtype-swift.enum.md)
  Types of browser column resizing.
- [Application Kit Versions for NSBrowser Functionality](../application-kit-versions-for-nsbrowser-functionality.md)
  The version of the AppKit.framework containing a specific bug fix or capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/dropoperation)*
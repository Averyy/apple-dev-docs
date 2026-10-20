# private

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A constant that indicates the source and destination negotiate the drag operation privately.

**Availability**:
- macOS

## Declaration

```swift
static var `private`: NSDragOperation { get }
```

```c
NSDragOperationPrivate
```

## See Also

### Constants
- [static var copy: NSDragOperation](./copy.md)
  A constant that indicates the drag can copy the data that the image represents.
- [static var link: NSDragOperation](./link.md)
  A constant that indicates the drag can share the data.
- [static var generic: NSDragOperation](./generic.md)
  A constant that indicates the destination can define the drag operation.
- [static var move: NSDragOperation](./move.md)
  A constant that indicates the drag can move the data.
- [static var delete: NSDragOperation](./delete.md)
  A constant that indicates the drag can delete the data.
- [static var every: NSDragOperation](./every.md)
  A constant that indicates that drag can perform all of the drag operations.
- [static var all: NSDragOperation](./all.md)
  Use [`every`](./every.md) instead.
- [static var all_Obsolete: NSDragOperation](./all_obsolete.md)
  The `NSDragOperationAll` constant is deprecated. Use [`every`](./every.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragoperation/private)*
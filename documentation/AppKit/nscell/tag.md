# tag

**Framework**: AppKit  
**Kind**: property

A tag for identifying the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var tag: Int { get set }
```

#### Discussion

Tags allow you to identify particular cells. Tag values are not used internally by AppKit. You typically set tag values in Interface Builder and use them at runtime in your application. When you set the tag of a control with a single cell in Interface Builder, it sets the tags of both the control and the cell to the same value as a convenience.

The default value of this property is `-1`. Setting the value of this property raises with [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException). Subclasses are expected to override this property if they support tags. The [`NSActionCell`](nsactioncell.md) class implements this property and stores the integer you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/tag)*
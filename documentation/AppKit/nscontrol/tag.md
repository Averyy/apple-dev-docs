# tag

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tag identifying the receiver (not the tag of the receiver’s cell).

**Availability**:
- macOS

## Declaration

```swift
var tag: Int { get set }
```

```objc
@property NSInteger tag;
```

#### Discussion

Tags allow you to identify particular controls. Tag values are not used internally; they are only changed when you set this property. You typically set tag values in Interface Builder and use them at runtime in your application. When you set the tag of a control with a single cell in Interface Builder, it sets the tags of both the control and the cell to the same value as a convenience.

## See Also

### Related Documentation
- [func selectedTag() -> Int](./selectedtag%28%29.md)
  Returns the tag of the receiver’s selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/tag)*
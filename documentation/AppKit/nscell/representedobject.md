# representedObject

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object represented by the cell.

**Availability**:
- macOS

## Declaration

```swift
var representedObject: Any? { get set }
```

```objc
@property (strong, nullable) id representedObject;
```

## Discussion

Use this property to link the cell an appropriate object. For example, in a pop-up list of color names, the represented object of each cell could be the appropriate [`NSColor`](../nscolor.md) object.

### Special Considerations

When you copy an `NSCell` object, the value of this property is set to `nil` in the copy.

## See Also

### Related Documentation
- [var objectValue: Any?](./objectvalue.md)
  The cell’s value as an Objective-C object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/representedobject)*
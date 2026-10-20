# selection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A proxy object representing the receiver’s selection.

**Availability**:
- macOS

## Declaration

```swift
var selection: Any { get }
```

```objc
@property (strong, readonly) id selection;
```

#### Discussion

This object is fully key-value coding compliant, but note that it is a proxy and so does not provide the full range of functionality that might be available in the source object.

## See Also

### Obtaining selections
- [var selectedObjects: [Any]](./selectedobjects.md)
  An array of all objects to be affected by editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/selection)*
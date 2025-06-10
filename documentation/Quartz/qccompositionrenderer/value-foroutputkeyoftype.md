# value(forOutputKey:ofType:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the current value on an output port (identified by its key) of the root patch of the composition.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func value(forOutputKey key: String!, ofType type: String!) -> Any!
```

#### Return Value

The value.

#### Discussion

The value type depends on the type of the port type, as shown in the following table

| Port type | Value type |
| --- | --- |
| Boolean, Index, or Number | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) or any object that responds to the methods `integerValue`, `floatValue`, or `doubleValue` |
| String | [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) or any object that responds to the methods`stringValue` or `description` |
| Color | [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor), [`CIColor`](https://developer.apple.com/documentation/CoreImage/CIColor), or `CGColor` object |
| Image | [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage), [`NSBitmapImageRep`](https://developer.apple.com/documentation/AppKit/NSBitmapImageRep), `CGImage` object, [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage), `CVPixelBuffer` object, `CVOpenGLBuffer` object, or an opaque `QCImage` (that is, an optimized abstract image object only to be used with `setValue:forInputKey:` of another `<QCCompositionRenderer>`) |
| Structure | [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) or [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) |

## Parameters

- `key`: The key associated with an output port for the root patch of a composition. This method throws an exception if   is invalid.
- `type`: A string that specifies the class.

## See Also

- [func setValue(Any!, forInputKey: String!) -> Bool](qccompositionrenderer/setvalue(_:forinputkey:).md)
  Sets the value for an input port of a composition.
- [func value(forInputKey: String!) -> Any!](qccompositionrenderer/value(forinputkey:).md)
  Returns the value for an input port of a composition.
- [func value(forOutputKey: String!) -> Any!](qccompositionrenderer/value(foroutputkey:).md)
  Returns the value for an output port of a composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/value(foroutputkey:oftype:))*
# value(forOutputKey:ofType:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the current value on an output port (identified by its key) of the root patch of the composition.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func value(forOutputKey key: String!, ofType type: String!) -> Any!
```

```objc
- (id) valueForOutputKey:(NSString *) key ofType:(NSString *) type;
```

#### Return Value

The value.

#### Discussion

The value type depends on the type of the port type, as shown in the following table

| Port type | Value type |
| --- | --- |
| Boolean, Index, or Number | [`NSNumber`](../../Foundation/nsnumber.md) or any object that responds to the methods `integerValue`, `floatValue`, or `doubleValue` |
| String | [`NSString`](../../Foundation/nsstring.md) or any object that responds to the methods`stringValue` or `description` |
| Color | [`NSColor`](../../AppKit/nscolor.md), [`CIColor`](../../CoreImage/cicolor.md), or `CGColor` object |
| Image | [`NSImage`](../../AppKit/nsimage.md), [`NSBitmapImageRep`](../../AppKit/nsbitmapimagerep.md), `CGImage` object, [`CIImage`](../../CoreImage/ciimage.md), `CVPixelBuffer` object, `CVOpenGLBuffer` object, or an opaque `QCImage` (that is, an optimized abstract image object only to be used with `setValue:forInputKey:` of another `<QCCompositionRenderer>`) |
| Structure | [`NSArray`](../../Foundation/nsarray.md) or [`NSDictionary`](../../Foundation/nsdictionary.md) |

## Parameters

- `key`: The key associated with an output port for the root patch of a composition. This method throws an exception if `key` is invalid.
- `type`: A string that specifies the class.

## See Also

### Passing and Retrieving Values From a Composition
- [func setValue(Any!, forInputKey: String!) -> Bool](./setvalue%28_,forinputkey%29.md)
  Sets the value for an input port of a composition.
- [func value(forInputKey: String!) -> Any!](./value%28forinputkey%29.md)
  Returns the value for an input port of a composition.
- [func value(forOutputKey: String!) -> Any!](./value%28foroutputkey%29.md)
  Returns the value for an output port of a composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/value(foroutputkey:oftype:))*
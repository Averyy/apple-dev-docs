# name

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The display’s name that you specified at creation time.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var name: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * name;
```

## See Also

### Inspecting Display Properties
- [var serialNum: UInt32](./serialnum.md)
  The display’s serial number that you specified at creation time.
- [var port: Int](./port.md)
  The display’s accelerator port that you specified at creation time.
- [var sizeInMillimeters: NSSize](./sizeinmillimeters.md)
  The display’s virtual dimensions, in millimeters, that you specified at creation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/name)*
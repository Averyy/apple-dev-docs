# port

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The display’s accelerator port that you specified at creation time.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var port: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger port;
```

## See Also

### Inspecting Display Properties
- [var name: String?](./name.md)
  The display’s name that you specified at creation time.
- [var serialNum: UInt32](./serialnum.md)
  The display’s serial number that you specified at creation time.
- [var sizeInMillimeters: NSSize](./sizeinmillimeters.md)
  The display’s virtual dimensions, in millimeters, that you specified at creation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/port)*
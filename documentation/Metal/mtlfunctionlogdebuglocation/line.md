# line

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The line that the log message appears on.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var line: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger line;
```

## See Also

### Inspecting the location details
- [var functionName: String?](./functionname.md)
  The name of the shader function.
- [var url: URL?](./url.md)
  The URL of the file that contains the shader function.
- [var column: Int](./column.md)
  The column where the log message appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionlogdebuglocation/line)*
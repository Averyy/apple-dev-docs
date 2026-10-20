# functionName

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The name of the shader function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var functionName: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * functionName;
```

## See Also

### Inspecting the location details
- [var url: URL?](./url.md)
  The URL of the file that contains the shader function.
- [var line: Int](./line.md)
  The line that the log message appears on.
- [var column: Int](./column.md)
  The column where the log message appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionlogdebuglocation/functionname)*
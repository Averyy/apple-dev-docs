# installName

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A file path for this dynamic library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var installName: String { get }
```

```objc
@property (readonly) NSString * installName;
```

## See Also

### Identifying the library
- [var device: any MTLDevice](./device.md)
  The Metal device object that created the dynamic library.
- [var label: String?](./label.md)
  A string that identifies the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldynamiclibrary/installname)*
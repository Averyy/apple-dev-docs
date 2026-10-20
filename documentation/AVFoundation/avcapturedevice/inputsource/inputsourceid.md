# inputSourceID

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An identifier for an input source.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var inputSourceID: String { get }
```

```objc
@property (nonatomic, readonly) NSString * inputSourceID;
```

#### Discussion

The identifier is unique among the input sources exposed by particular capture device instance.

## See Also

### Accessing properties
- [var localizedName: String](./localizedname.md)
  A localized, human-readable name for the input source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/inputsource/inputsourceid)*
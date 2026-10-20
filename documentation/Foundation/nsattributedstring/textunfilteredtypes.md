# textUnfilteredTypes

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An array of UTI strings that identify the file types that attributed strings support directly.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class var textUnfilteredTypes: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * textUnfilteredTypes;
```

#### Return Value

An array of `NSString` objects, each of which contains a UTI identifying a supported file type.

#### Discussion

The returned list includes UTI strings only for those file types that are supported directly by the receiver. It does not include types that are supported through user-installed filter services. You can use the returned UTI strings with any method that supports UTIs.

## See Also

### Getting the supported text-file formats
- [func prefersRTFD(in: NSRange) -> Bool](./prefersrtfd%28in%29.md)
  Returns a Boolean value that indicates whether the specified range of text prefers RTFD formatting.
- [class var textTypes: [String]](./texttypes.md)
  An array of UTI strings that identify the file types that attributed strings support, either directly or through a user-installed filter service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/textunfilteredtypes)*
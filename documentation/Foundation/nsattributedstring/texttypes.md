# textTypes

**Framework**: Foundation  
**Kind**: property

An array of UTI strings that identify the file types that attributed strings support, either directly or through a user-installed filter service.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class var textTypes: [String] { get }
```

#### Return Value

An array of `NSString` objects, each of which contains a UTI identifying a supported file type.

#### Discussion

The returned list includes UTIs all file types supported by the receiver plus those that can be opened by the receiver after being converted by a user-installed filter service. You can use the returned UTI strings with any method that supports UTIs.

## See Also

- [func prefersRTFD(in: NSRange) -> Bool](nsattributedstring/prefersrtfd(in:).md)
  Returns a Boolean value that indicates whether the specified range of text prefers RTFD formatting.
- [class var textUnfilteredTypes: [String]](nsattributedstring/textunfilteredtypes.md)
  An array of UTI strings that identify the file types that attributed strings support directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/texttypes)*
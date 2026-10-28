# prefersRTFD(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the specified range of text prefers RTFD formatting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func prefersRTFD(in range: NSRange) -> Bool
```

```objc
- (BOOL) prefersRTFDInRange:(NSRange) range;
```

## Return Value

[`true`](../../Swift/true.md) if the range of text prefers RTFD formatting, or [`false`](../../Swift/false.md) if you can use the RTF format instead.

## Discussion

When an attributed string contains attachments, you must save it using the RTFD file format to preserve the attached files.

## Parameters

- `range`: The range of text to test.

## See Also

### Getting the supported text-file formats
- [class var textTypes: [String]](./texttypes.md)
  An array of UTI strings that identify the file types that attributed strings support, either directly or through a user-installed filter service.
- [class var textUnfilteredTypes: [String]](./textunfilteredtypes.md)
  An array of UTI strings that identify the file types that attributed strings support directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/prefersrtfd(in:))*
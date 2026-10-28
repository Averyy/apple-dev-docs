# init(data:ofType:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a text attachment object with the specified data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(data contentData: Data?, ofType uti: String?)
```

```objc
- (instancetype) initWithData:(NSData *) contentData ofType:(NSString *) uti;
```

## Return Value

A new `NSTextAttachment` object.

## Discussion

This method is the designated initializer for the `NSTextAttachment` class on iOS.

When either `contentData` or `uti` is `nil`, TextKit considers the receiver to be an attachment without document contents. In this case, the `NSAttributedString` external file writing methods try to save the value of the [`image`](./image.md) property instead.

## Parameters

- `contentData`: Data to use for the text attachment contents. Can be `nil`.
- `uti`: A uniform type identifier specifying the data type of the attachment contents. Can be `nil`.

## See Also

### Initializing a text attachment
- [convenience init(fileWrapper: FileWrapper?)](../../AppKit/nstextattachment/init%28filewrapper%29.md)
  Creates a text attachment object to contain the specified file wrapper.
- [init(image: UIImage)](./init%28image%29.md)
  Creates a text attachment object to contain the specified image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachment/init(data:oftype:))*
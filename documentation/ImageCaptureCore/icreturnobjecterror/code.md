# ICReturnObjectError.Code

**Framework**: ImageCaptureCore  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum Code
```

```c
enum ICReturnObjectErrorCode : NSInteger;
```

## Topics

### Enumeration Cases
- [ICReturnObjectError.Code.codeObjectCouldNotBeRead](./code/codeobjectcouldnotberead.md)
  The object could not be read.
- [ICReturnObjectError.Code.codeObjectDataEmpty](./code/codeobjectdataempty.md)
  The object data is empty.
- [ICReturnObjectError.Code.codeObjectDataOffsetInvalid](./code/codeobjectdataoffsetinvalid.md)
  The object data offset is invalid.
- [ICReturnObjectError.Code.codeObjectDataRequestTooLarge](./code/codeobjectdatarequesttoolarge.md)
- [ICReturnObjectError.Code.codeObjectDoesNotExist](./code/codeobjectdoesnotexist.md)
  The object does not exist.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Error Codes
- [static var codeObjectDoesNotExist: ICReturnObjectError.Code](./codeobjectdoesnotexist.md)
  The object does not exist.
- [static var codeObjectDataOffsetInvalid: ICReturnObjectError.Code](./codeobjectdataoffsetinvalid.md)
  The object data offset is invalid.
- [static var codeObjectCouldNotBeRead: ICReturnObjectError.Code](./codeobjectcouldnotberead.md)
  The object could not be read.
- [static var codeObjectDataEmpty: ICReturnObjectError.Code](./codeobjectdataempty.md)
  The object data is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturnobjecterror/code)*
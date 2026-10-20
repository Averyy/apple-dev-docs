# SSReadingListError.Code

**Framework**: Safari Services  
**Kind**: enum  
**Role**: Enumeration

Messages that describe a Safari Reading List error.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
enum Code
```

*Mac Catalyst*

```swift
enum SSReadingListErrorCode
```

```c
enum SSReadingListErrorCode : NSInteger;
```

## Topics

### Constants
- [SSReadingListError.Code.urlSchemeNotAllowed](./code/urlschemenotallowed.md)
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

### Safari Reading List
- [class SSReadingList](../ssreadinglist.md)
  An object for adding items to a user’s Safari Reading List.
- [let SSReadingListErrorDomain: String](../ssreadinglisterrordomain.md)
  The domain for Safari Reading List errors.
- [struct SSReadingListError](../ssreadinglisterror.md)
  A Safari Reading List error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/ssreadinglisterror/code)*
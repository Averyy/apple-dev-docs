# headers

**Framework**: MailKit  
**Kind**: property  
**Role**: Instance Property

A dictionary that contains the message’s header values.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var headers: [String : [String]]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSDictionary<NSString *,NSArray<NSString *> *> * headers;
```

#### Discussion

If MailKit hasn’t downloaded the full message, this dictionary may only contain a subset of the message’s headers.

## See Also

### Accessing Message Content
- [var rawData: Data?](./rawdata.md)
  The raw RFC 2822 header and body content of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessage/headers)*
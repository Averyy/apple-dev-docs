# CFStreamErrorHTTP.parseFailure

**Framework**: CFNetwork  
**Kind**: case  
**Role**: Case

A parsing error occurred while an incoming message was being deserialized and appended to a message object. The headers of the incoming message may be formatted improperly.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case parseFailure
```

```c
kCFStreamErrorHTTPParseFailure
```

## See Also

### Constants
- [CFStreamErrorHTTP.redirectionLoop](./redirectionloop.md)
  A redirection loop has been detected.
- [CFStreamErrorHTTP.badURL](./badurl.md)
  The URL is not properly formatted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfstreamerrorhttp/parsefailure)*
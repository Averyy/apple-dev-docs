# assumesHTTP3Capable

**Framework**: Foundation  
**Kind**: property

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
var assumesHTTP3Capable: Bool { get }
```

#### Return Value

YES if server endpoint is known to support HTTP/3. Defaults to NO. The default may be YES in a future OS update.

#### Discussion

Returns whether we assume that server supports HTTP/3. Enables QUIC racing without HTTP/3 service discovery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/assumeshttp3capable)*
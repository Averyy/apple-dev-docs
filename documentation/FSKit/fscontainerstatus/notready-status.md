# notReady(status:)

**Framework**: FSKit  
**Kind**: method

Returns a not-ready container status instance with the provided error status.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class func notReady(status errorStatus: any Error) -> Self
```

## Parameters

- `errorStatus`: The error status, if any, for the new instance.

## See Also

- [class func active(status: any Error) -> Self](fscontainerstatus/active(status:).md)
  Returns a active container status instance with the provided error status.
- [class func blocked(status: any Error) -> Self](fscontainerstatus/blocked(status:).md)
  Returns a blocked container status instance with the provided error status.
- [class func ready(status: any Error) -> Self](fscontainerstatus/ready(status:).md)
  Returns a ready container status instance with the provided error status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstatus/notready(status:))*
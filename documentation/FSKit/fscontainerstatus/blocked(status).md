# blocked(status:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Type Method

Returns a blocked container status instance with the provided error status.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class func blocked(status errorStatus: any Error) -> Self
```

```objc
+ (instancetype) blockedWithStatus:(NSError *) errorStatus;
```

## Parameters

- `errorStatus`: The error status, if any, for the new instance.

## See Also

### Creating a container status instance
- [class func active(status: any Error) -> Self](./active%28status%29.md)
  Returns a active container status instance with the provided error status.
- [class func notReady(status: any Error) -> Self](./notready%28status%29.md)
  Returns a not-ready container status instance with the provided error status.
- [class func ready(status: any Error) -> Self](./ready%28status%29.md)
  Returns a ready container status instance with the provided error status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstatus/blocked(status:))*
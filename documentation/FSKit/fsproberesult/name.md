# name

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The resource name, as found during the probe operation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var name: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * name;
```

#### Discussion

This value is non-`nil` unless the [`result`](./result.md) is ``FSMatchResult/notRecognized`. For formats that lack a name, this value may be an empty string. This value can also be an empty string if the format supports a name, but the value isn’t set yet.

## See Also

### Working with result properties
- [var containerID: FSContainerIdentifier?](./containerid.md)
  The container identifier, as found during the probe operation.
- [var result: FSMatchResult](./result.md)
  The match result, representing the recognition and usability of a probed resource.
- [enum FSMatchResult](../fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult/name)*
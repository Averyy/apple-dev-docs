# name

**Framework**: FSKit  
**Kind**: property

The resource name, as found during the probe operation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var name: String? { get }
```

#### Discussion

This value is non-`nil` unless the [`result`](fsproberesult/result.md) is ``FSMatchResult/notRecognized`. For formats that lack a name, this value may be an empty string. This value can also be an empty string if the format supports a name, but the value isn’t set yet.

## See Also

- [var containerID: FSContainerIdentifier?](fsproberesult/containerid.md)
  The container identifier, as found during the probe operation.
- [var result: FSMatchResult](fsproberesult/result.md)
  The match result, representing the recognition and usability of a probed resource.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult/name)*
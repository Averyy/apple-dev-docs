# containerID

**Framework**: FSKit  
**Kind**: property

The container identifier, as found during the probe operation.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var containerID: FSContainerIdentifier? { get }
```

#### Discussion

This value is non-`nil` unless the result is [`FSMatchResult.notRecognized`](fsmatchresult/notrecognized.md). For formats that lack a durable UUID on which to base a container identifier — which is only legal for a [`FSUnaryFileSystem`](fsunaryfilesystem.md) — this value may be a random UUID.

## See Also

- [var name: String?](fsproberesult/name.md)
  The resource name, as found during the probe operation.
- [var result: FSMatchResult](fsproberesult/result.md)
  The match result, representing the recognition and usability of a probed resource.
- [enum FSMatchResult](fsmatchresult.md)
  A type that represents the recognition and usability of a probed resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult/containerid)*
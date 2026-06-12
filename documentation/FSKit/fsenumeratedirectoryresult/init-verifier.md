# init(verifier:)

**Framework**: FSKit  
**Kind**: init

Creates a result for an directory enumeration operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(verifier currentVerifier: UInt64)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `currentVerifier`: An `FSDirectoryVerifier` value that reflects the directory’s current version. FSKit uses this value to detect whether the directory contents changed since the last enumeration call.

## See Also

- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsenumeratedirectoryresult/init(verifier:))*
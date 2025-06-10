# init(keySystem:storageDirectoryAt:)

**Framework**: AVFoundation  
**Kind**: init

Creates a content key session to manage a collection of content decryption keys; points to a directory that stores abnormal session termination reports.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(keySystem: AVContentKeySystem, storageDirectoryAt storageURL: URL)
```

#### Return Value

Returns a new AVContentKeySession instance.

#### Discussion

The `AVContentKeySession` instance returned is capable of managing a collection of content decryption keys that correspond to the input key system. An [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) is raised when the value of `keySystem` is unsupported.

## Parameters

- `keySystem`: A valid key system used to retrieve keys.
- `storageURL`: A URL that points to a writable directory. The session uses the directory to facilitate expired session reports after an abnormal session termination.

## See Also

- [convenience init(keySystem: AVContentKeySystem)](avcontentkeysession/init(keysystem:).md)
  Creates a content key session to manage a collection of content decryption keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/init(keysystem:storagedirectoryat:))*
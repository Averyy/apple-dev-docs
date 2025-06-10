# init(keySystem:)

**Framework**: AVFoundation  
**Kind**: init

Creates a content key session to manage a collection of content decryption keys.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(keySystem: AVContentKeySystem)
```

#### Return Value

Returns a new [`AVContentKeySession`](avcontentkeysession.md) instance.

#### Discussion

The `AVContentKeySession` instance returned is capable of managing a collection of content decryption keys that correspond to the input key system. An [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) is raised when the value of `keySystem` is unsupported.

## Parameters

- `keySystem`: A valid key system used to retrieve keys.

## See Also

- [convenience init(keySystem: AVContentKeySystem, storageDirectoryAt: URL)](avcontentkeysession/init(keysystem:storagedirectoryat:).md)
  Creates a content key session to manage a collection of content decryption keys; points to a directory that stores abnormal session termination reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/init(keysystem:))*
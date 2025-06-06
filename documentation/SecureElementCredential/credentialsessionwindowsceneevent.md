# CredentialSessionWindowSceneEvent

**Framework**: SecureElementCredential  
**Kind**: enum

An event that a credential session sends to a UIKit scene.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum CredentialSessionWindowSceneEvent
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

## Topics

### Events
- [CredentialSessionWindowSceneEvent.presentation](credentialsessionwindowsceneevent/presentation.md)
  The user performs a gesture, such as double-pressing the side button, to present an NFC display.
- [CredentialSessionWindowSceneEvent.readerDetected](credentialsessionwindowsceneevent/readerdetected.md)
  The eligible device detects the RF field of an NFC reader.
### Describing the event
- [var description: String](credentialsessionwindowsceneevent/description.md)
  A textual representation of this instance.
### Encoding and decoding
- [init(from: any Decoder) throws](credentialsessionwindowsceneevent/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](credentialsessionwindowsceneevent/encode(to:).md)
  Encodes this value into the given encoder.
### Hashing
- [func hash(into: inout Hasher)](credentialsessionwindowsceneevent/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](credentialsessionwindowsceneevent/hashvalue.md)
  The hash value.
### Comparing events
- [static func == (CredentialSessionWindowSceneEvent, CredentialSessionWindowSceneEvent) -> Bool](credentialsessionwindowsceneevent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](credentialsessionwindowsceneevent/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func windowScene(UIWindowScene, didReceiveCredentialSessionWindowSceneEvent: CredentialSessionWindowSceneEvent)](credentialsessionwindowscenedelegate/windowscene(_:didreceivecredentialsessionwindowsceneevent:).md)
  Informs your app that a credential session event initiated a UIKit scene creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsessionwindowsceneevent)*
# name

**Framework**: HomeKit  
**Kind**: property

The name of the action set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

Action set names must be unique within a home.

## See Also

- [HomeKit Developer Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40015050)
- [var uniqueIdentifier: UUID](hmactionset/uniqueidentifier.md)
  The action set’s unique identifier.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmactionset/updatename(_:completionhandler:).md)
  Updates the name of the action set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/name)*
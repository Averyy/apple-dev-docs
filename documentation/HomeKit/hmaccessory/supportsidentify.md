# supportsIdentify

**Framework**: HomeKit  
**Kind**: property

A Boolean value that indicates whether the accessory supports the identify action.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- tvOS 11.3+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
var supportsIdentify: Bool { get }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/swift/false), any calls to the [`identify(completionHandler:)`](hmaccessory/identify(completionhandler:).md) method return an error. However, even if this property is [`true`](https://developer.apple.com/documentation/swift/true), calls to [`identify(completionHandler:)`](hmaccessory/identify(completionhandler:).md) may not succeed.

## See Also

- [func identify(completionHandler: ((any Error)?) -> Void)](hmaccessory/identify(completionhandler:).md)
  Asks an accessory to identify itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/supportsidentify)*
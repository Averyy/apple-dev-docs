# supportsIdentify

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL supportsIdentify;
```

## Discussion

If [`false`](../../Swift/false.md), any calls to the [`identify(completionHandler:)`](./identify%28completionhandler%29.md) method return an error. However, even if this property is [`true`](../../Swift/true.md), calls to [`identify(completionHandler:)`](./identify%28completionhandler%29.md) may not succeed.

## See Also

### Asking an accessory to identify itself
- [func identify(completionHandler: ((any Error)?) -> Void)](./identify%28completionhandler%29.md)
  Asks an accessory to identify itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/supportsidentify)*
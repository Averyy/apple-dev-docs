# identify(completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Asks an accessory to identify itself.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func identify() async throws
```

#### Discussion

Accessories typically identify themselves by briefly doing something the user can see or hear. The behavior is specific to the device. For example, a light bulb might identify itself by briefly turning on if it is currently off, or by briefly dimming if it is currently on. This can help a user pinpoint one device among several that are similar.

## Parameters

- `completion`: Block that is invoked once the request is processed.

## See Also

- [var supportsIdentify: Bool](hmaccessory/supportsidentify.md)
  A Boolean value that indicates whether the accessory supports the identify action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/identify(completionhandler:))*
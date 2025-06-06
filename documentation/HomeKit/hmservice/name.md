# name

**Framework**: HomeKit  
**Kind**: property

The user specified name of the service.

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

Rename services by calling the [`updateName(_:completionHandler:)`](hmservice/updatename(_:completionhandler:).md) method with a value given by the user.

## See Also

- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmservice/updatename(_:completionhandler:).md)
  Updates the name of the service to the specified string.
- [var uniqueIdentifier: UUID](hmservice/uniqueidentifier.md)
  A unique identifier for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservice/name)*
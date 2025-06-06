# SMLoginItemSetEnabled(_:_:)

**Framework**: Service Management  
**Kind**: func

Enables a helper executable in the main app-bundle directory.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func SMLoginItemSetEnabled(_ identifier: CFString, _ enabled: Bool) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the requested change has taken effect.

#### Discussion

> ❗ **Important**:  To enable or disable `LoginItems` in macOS 13 and later, use the [`register()`](smappservice/register().md) and [`unregister()`](smappservice/unregister().md) methods instead.

 To enable or disable `LoginItems` in macOS 13 and later, use the [`register()`](smappservice/register().md) and [`unregister()`](smappservice/unregister().md) methods instead.

The build system places helper executables in the app’s bundle in the `Contents/Library/LoginItems` directory.

## Parameters

- `identifier`: The identifier of the helper executable bundle.
- `enabled`: A Boolean value that represents the state of the helper executable. This value is effective only for the currently logged-in user. If  , the helper tool executable immediately (and upon subsequent logins) and keeps running. If  , the helper executable stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smloginitemsetenabled(_:_:))*
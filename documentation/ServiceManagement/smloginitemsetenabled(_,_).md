# SMLoginItemSetEnabled(_:_:)

**Framework**: Service Management  
**Kind**: func  
**Role**: Function

Enables a helper executable in the main app-bundle directory.

**Availability**:
- macOS 10.6+ - Deprecated in 13.0

> **Deprecated**: Please use SMAppService instead

## Declaration

```swift
func SMLoginItemSetEnabled(_ identifier: CFString, _ enabled: Bool) -> Bool
```

```c
extern Boolean SMLoginItemSetEnabled(CFStringRef identifier, Boolean enabled);
```

## Return Value

Returns [`true`](../Swift/true.md) if the requested change has taken effect.

## Discussion

> ❗ **Important**:  To enable or disable `LoginItems` in macOS 13 and later, use the [`register()`](./smappservice/register%28%29.md) and [`unregister()`](./smappservice/unregister%28%29.md) methods instead.

The build system places helper executables in the app’s bundle in the `Contents/Library/LoginItems` directory.

## Parameters

- `identifier`: The identifier of the helper executable bundle.
- `enabled`: A Boolean value that represents the state of the helper executable. This value is effective only for the currently logged-in user. If [`true`](../Swift/true.md), the helper tool executable immediately (and upon subsequent logins) and keeps running. If [`false`](../Swift/false.md), the helper executable stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smloginitemsetenabled(_:_:))*
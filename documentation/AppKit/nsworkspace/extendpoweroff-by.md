# extendPowerOff(by:)

**Framework**: AppKit  
**Kind**: method

Requests the system wait for the specified amount of time before turning off the power or logging out the user.

**Availability**:
- macOS ?+

## Declaration

```swift
func extendPowerOff(by requested: Int) -> Int
```

#### Return Value

The number of milliseconds granted by the system. This method currently returns `0`.

#### Discussion

This method currently does nothing. Do not call it.

## Parameters

- `requested`: The number of milliseconds to wait before turning off the power or logging off the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/extendpoweroff(by:))*
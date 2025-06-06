# environment(_:stateDidChangeFromOldState:)

**Framework**: Local Authentication  
**Kind**: method

Called when there has been a change in the environment.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
optional func environment(_ environment: LAEnvironment, stateDidChangeFromOldState oldState: LAEnvironment.State)
```

#### Discussion

Invoked on a queue private to LocalAuthentication framework. At the moment of invocation of this method, @c LAEnvironment.state already contains the new updated state.

## Parameters

- `oldState`: The old environment state (before update)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/observer/environment(_:statedidchangefromoldstate:))*
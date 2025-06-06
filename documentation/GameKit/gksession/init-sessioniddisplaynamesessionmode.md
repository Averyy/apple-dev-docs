# init(sessionID:displayName:sessionMode:)

**Framework**: GameKit  
**Kind**: init

Initializes and returns a newly allocated session.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init!(sessionID: String!, displayName name: String!, sessionMode mode: GKSessionMode)
```

#### Return Value

An initialized session object, or `nil` if an error occurred.

#### Discussion

Only sessions running with the same `sessionID` are visible to your session.

## Parameters

- `sessionID`: A unique string that identifies your application. Your   should be the short name of an approved Bonjour service type. If  , the session uses the application’s bundle identifier to create a   string.
- `name`: A string identifying the user to display to other peers. If  , the session uses the device name.
- `mode`: The mode the session should run in. See   for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/init(sessionid:displayname:sessionmode:))*
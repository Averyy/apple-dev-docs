# init(sessionID:displayName:sessionMode:)

**Framework**: GameKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly allocated session.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 2.0

> **Deprecated**: No longer available

## Declaration

```swift
init!(sessionID: String!, displayName name: String!, sessionMode mode: GKSessionMode)
```

```objc
- (id) initWithSessionID:(NSString *) sessionID displayName:(NSString *) name sessionMode:(GKSessionMode) mode;
```

#### Return Value

An initialized session object, or `nil` if an error occurred.

#### Discussion

Only sessions running with the same `sessionID` are visible to your session.

## Parameters

- `sessionID`: A unique string that identifies your application. Your `sessionID` should be the short name of an approved Bonjour service type. If `nil`, the session uses the application’s bundle identifier to create a `sessionID` string.
- `name`: A string identifying the user to display to other peers. If `nil`, the session uses the device name.
- `mode`: The mode the session should run in. See [`GKSessionMode`](../gksessionmode.md) for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/init(sessionid:displayname:sessionmode:))*
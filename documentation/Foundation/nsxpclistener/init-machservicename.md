# init(machServiceName:)

**Framework**: Foundation  
**Kind**: init

Initializes a listener in a LaunchAgent or LaunchDaemon which has a name advertised in a `launchd.plist` file.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(machServiceName name: String)
```

#### Discussion

For example, you might use this in an agent launched by launchd with a `launchd.plist` contained in `~/Library/LaunchAgents`, or a daemon launched by launchd with a `launchd.plist` contained in `/Library/LaunchDaemons`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/init(machservicename:))*
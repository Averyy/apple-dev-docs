# init(machServiceName:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a listener in a LaunchAgent or LaunchDaemon which has a name advertised in a `launchd.plist` file.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(machServiceName name: String)
```

```objc
- (instancetype) initWithMachServiceName:(NSString *) name;
```

## Discussion

For example, you might use this in an agent launched by launchd with a `launchd.plist` contained in `~/Library/LaunchAgents`, or a daemon launched by launchd with a `launchd.plist` contained in `/Library/LaunchDaemons`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/init(machservicename:))*
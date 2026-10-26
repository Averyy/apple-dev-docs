# init()

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Initializes a new world-tracking configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Discussion

To use the configuration in an AR experience, pass it as an argument to your app’s [`run(_:options:)`](../arsession/run%28_,options%29.md) function.

## See Also

### Creating a Configuration
- [var initialWorldMap: ARWorldMap?](./initialworldmap.md)
  The state from a previous AR session to attempt to resume with this session configuration.
- [+ new](./new.md)
  Creates a new world-tracking configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/init())*
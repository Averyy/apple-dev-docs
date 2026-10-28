# new

**Framework**: ARKit  
**Kind**: method  
**Role**: Type Method

Creates a new world-tracking configuration.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```objc
+ (instancetype) new;
```

## Discussion

To use the configuration in an AR experience, pass it as an argument to your app’s [`run(_:options:)`](../arsession/run%28_,options%29.md) function.

## See Also

### Creating a Configuration
- [init()](./init%28%29.md)
  Initializes a new world-tracking configuration.
- [var initialWorldMap: ARWorldMap?](./initialworldmap.md)
  The state from a previous AR session to attempt to resume with this session configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/new)*
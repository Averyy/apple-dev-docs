# LAEnvironment.Observer

**Framework**: Local Authentication  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol Observer : NSObjectProtocol
```

```objc
@protocol LAEnvironmentObserver <NSObject>
```

## Topics

### Instance Methods
- [func environment(LAEnvironment, stateDidChangeFromOldState: LAEnvironment.State)](./observer/environment%28_,statedidchangefromoldstate%29.md)
  Called when there has been a change in the environment.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/observer)*
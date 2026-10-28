# shared

**Framework**: Intents  
**Kind**: property  
**Role**: Type Property

The shared upcoming media manager.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class var shared: INUpcomingMediaManager { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (class, nonatomic, readonly) INUpcomingMediaManager * sharedManager;
```

*macOS*

```objc
@property (class, atomic, readonly) INUpcomingMediaManager * sharedManager;
```

## Discussion

Always use the shared upcoming media manager instead of creating an instance of [`INUpcomingMediaManager`](../inupcomingmediamanager.md) with an initializer method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupcomingmediamanager/shared)*
# BGAppRefreshTask

**Framework**: Background Tasks  
**Kind**: class

An object representing a short task typically used to refresh content that’s run while the app is in the background.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class BGAppRefreshTask
```

## Mentions

- [Choosing Background Strategies for Your App](choosing-background-strategies-for-your-app.md)

#### Overview

Use app refresh tasks for updating your app with small bits of information, such as the latest stock values.

Executing app refresh tasks requires setting the `fetch` [`UIBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIBackgroundModes) capability. For information on setting this capability, see [`BGTaskScheduler`](bgtaskscheduler.md).

## Relationships

### Inherits From
- [BGTask](bgtask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BGProcessingTask](bgprocessingtask.md)
  A time-consuming processing task that runs while the app is in the background.
- [class BGTask](bgtask.md)
  An abstract class representing a task that’s run while the app is in the background.
- [class BGHealthResearchTask](bghealthresearchtask.md)
  A time-consuming, necessary processing task that runs while the app is in the background to prepare data essential to a health research study.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtask)*
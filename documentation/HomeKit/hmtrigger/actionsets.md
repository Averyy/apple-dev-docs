# actionSets

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

Array of all action sets that will be executed by the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var actionSets: [HMActionSet] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMActionSet *> * actionSets;
```

#### Discussion

Action sets are instances of [`HMActionSet`](../hmactionset.md).

## See Also

### Managing Action Sets
- [func addActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./addactionset%28_,completionhandler%29.md)
  Adds an action set to the trigger.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./removeactionset%28_,completionhandler%29.md)
  Removes an action set from the trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/actionsets)*
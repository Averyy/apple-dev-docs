# qualityOfService

**Framework**: Foundation  
**Kind**: property

The relative amount of importance for granting system resources to the operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var qualityOfService: QualityOfService { get set }
```

#### Discussion

Service levels affect the priority with which an operation object is given access to system resources such as CPU time, network resources, disk resources, and so on. Operations with a higher quality of service level are given greater priority over system resources so that they may perform their task more quickly. You use service levels to ensure that operations responding to explicit user requests are given priority over less critical work.

This property reflects the minimum service level needed to execute the operation effectively. The default value of this property is [`QualityOfService.default`](qualityofservice/default.md) and you should leave that value in place whenever possible. When changing the service level, use the minimum level that is appropriate for executing the corresponding task. For example, if the user initiates a task and is waiting for it to finish, assign the value [`QualityOfService.userInteractive`](qualityofservice/userinteractive.md) to this property. The system may give the operation a higher service level to the operation if the resources are available to do so. For additional information, see [`Prioritize Work with Quality of Service Classes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html#//apple_ref/doc/uid/TP40015243-CH39) in [`Energy Efficiency Guide for iOS Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243) and [`Prioritize Work at the Task Level`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

## See Also

- [var threadPriority: Double](operation/threadpriority.md)
  The thread priority to use when executing the operation
- [var queuePriority: Operation.QueuePriority](operation/queuepriority-swift.property.md)
  The execution priority of the operation in an operation queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/qualityofservice)*
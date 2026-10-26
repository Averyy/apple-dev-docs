---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocktaskviewdelegate"
framework: "CareKit/CareKitUI"
---

# OCKTaskViewDelegate

**Framework**: CareKit/CareKitUI  
**Kind**: protocol  
**Role**: Protocol

A protocol that handles events related to a task object.

## Declaration

```swift
protocol OCKTaskViewDelegate : AnyObject
```

## Topics

### Instance Methods
- [func didSelectTaskView(UIView & OCKTaskDisplayable, eventIndexPath: IndexPath)](./ocktaskviewdelegate/didselecttaskview%28_,eventindexpath%29.md)
  Tells the delegate that the conforming object selected the task view.
- [func taskView(UIView & OCKTaskDisplayable, didCompleteEvent: Bool, at: IndexPath, sender: Any?)](./ocktaskviewdelegate/taskview%28_,didcompleteevent,at,sender%29.md)
  Tells the delegate that an event is completed.
- [func taskView(UIView & OCKTaskDisplayable, didCreateOutcomeValueAt: Int, eventIndexPath: IndexPath, sender: Any?)](./ocktaskviewdelegate/taskview%28_,didcreateoutcomevalueat,eventindexpath,sender%29.md)
  Tells the delegate that the conforming object created a value at a particular index.
- [func taskView(UIView & OCKTaskDisplayable, didSelectOutcomeValueAt: Int, eventIndexPath: IndexPath, sender: Any?)](./ocktaskviewdelegate/taskview%28_,didselectoutcomevalueat,eventindexpath,sender%29.md)
  Tells the delegate that the conforming object selected the outcome value for a particular event.

## See Also

### Task-interaction broadcasting
- [protocol OCKTaskDisplayable](./ocktaskdisplayable.md)
  Any object that can display and handle interactions with a task.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocktaskviewdelegate)*
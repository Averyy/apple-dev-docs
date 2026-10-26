---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocktaskviewdelegate/taskview(_:didselectoutcomevalueat:eventindexpath:sender:)"
framework: "CareKit/CareKitUI"
---

# taskView(_:didSelectOutcomeValueAt:eventIndexPath:sender:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the conforming object selected the outcome value for a particular event.

## Declaration

```swift
func taskView(_ taskView: UIView & OCKTaskDisplayable, didSelectOutcomeValueAt index: Int, eventIndexPath: IndexPath, sender: Any?)
```

## Parameters

- `taskView`: View displaying the outcome value.
- `index`: Index of the outcome value in the event’s outcome.
- `eventIndexPath`: Index path of the event.
- `sender`: Sender that initiated the selection.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocktaskviewdelegate/taskview(_:didselectoutcomevalueat:eventindexpath:sender:))*
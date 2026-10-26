---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocktaskviewdelegate/taskview(_:didcreateoutcomevalueat:eventindexpath:sender:)"
framework: "CareKit/CareKitUI"
---

# taskView(_:didCreateOutcomeValueAt:eventIndexPath:sender:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the conforming object created a value at a particular index.

## Declaration

```swift
func taskView(_ taskView: UIView & OCKTaskDisplayable, didCreateOutcomeValueAt index: Int, eventIndexPath: IndexPath, sender: Any?)
```

## Parameters

- `taskView`: View displaying the outcome.
- `index`: Index of the new outcome value.
- `eventIndexPath`: Index of the event.
- `sender`: Sender that initiated the outcome value creation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocktaskviewdelegate/taskview(_:didcreateoutcomevalueat:eventindexpath:sender:))*
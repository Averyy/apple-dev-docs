---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocktaskviewdelegate/taskview(_:didcompleteevent:at:sender:)"
framework: "CareKit/CareKitUI"
---

# taskView(_:didCompleteEvent:at:sender:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that an event is completed.

## Declaration

```swift
func taskView(_ taskView: UIView & OCKTaskDisplayable, didCompleteEvent isComplete: Bool, at indexPath: IndexPath, sender: Any?)
```

## Parameters

- `taskView`: View displaying the event.
- `isComplete`: True if the event is complete.
- `indexPath`: Index path of the event.
- `sender`: Sender that initiated the completion.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocktaskviewdelegate/taskview(_:didcompleteevent:at:sender:))*
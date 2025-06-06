# handle(_:)

**Framework**: Network Extension  
**Kind**: method

Receives a report from the framework.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func handle(_ report: NEFilterReport)
```

#### Discussion

The framework calls this method when the data provider extension returns a verdict with the [`shouldReport`](nefilterverdict/shouldreport.md) property set to [`true`](https://developer.apple.com/documentation/swift/true). Override this method in a subclass if you want to handle the flow report.

## Parameters

- `report`: The report delivered from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterprovider/handle(_:))*
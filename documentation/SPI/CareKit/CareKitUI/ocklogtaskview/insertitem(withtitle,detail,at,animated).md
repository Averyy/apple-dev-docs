---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklogtaskview/insertitem(withtitle:detail:at:animated:)"
framework: "CareKit/CareKitUI"
---

# insertItem(withTitle:detail:at:animated:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inserts an item in the list of logged items.

## Declaration

```swift
@discardableResult
@MainActor func insertItem(withTitle title: String?, detail: String?, at index: Int, animated: Bool) -> OCKLogItemButton
```

#### Return Value

The item that was inserted.

## Parameters

- `title`: The title text to display in the item.
- `detail`: The detail text to display in the item. The text is tinted by default.
- `index`: The index to insert the item in the list of logged items.
- `animated`: Animate the insertion of the logged item.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklogtaskview/insertitem(withtitle:detail:at:animated:))*
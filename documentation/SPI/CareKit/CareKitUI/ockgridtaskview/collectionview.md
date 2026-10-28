---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockgridtaskview/collectionview"
framework: "CareKit/CareKitUI"
---

# collectionView

**Framework**: CareKit/CareKitUI  
**Kind**: property  
**Role**: Instance Property

A collection view that sizes itself based on the size of its content.

## Declaration

```swift
@MainActor
lazy var collectionView: UICollectionView { get set }
```

## Discussion

Ensure that cells have a constant width constraint. The default cell is an `OCKGridTaskView.DefaultCellType` (`OCKGridTaskCell`). Set a data source to control the content of the grid.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockgridtaskview/collectionview)*
# onInsert(of:perform:)

**Framework**: SwiftUI  
**Kind**: method

Sets the insert action for the dynamic view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func onInsert(of acceptedTypeIdentifiers: [String], perform action: @escaping (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent
```

#### Return Value

A view that calls `action` when elements are inserted into the original view.

## Parameters

- `acceptedTypeIdentifiers`: An array of UTI types that the dynamic   view supports.
- `action`: A closure that SwiftUI invokes when elements are added to   the view. The closure takes two arguments: The first argument is the   offset relative to the dynamic view’s underlying collection of data.   The second argument is an array of   that represents   the data that you want to insert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)-40hwa)*
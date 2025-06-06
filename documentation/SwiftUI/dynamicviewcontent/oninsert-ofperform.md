# onInsert(of:perform:)

**Framework**: SwiftUI  
**Kind**: method

Sets the insert action for the dynamic view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func onInsert(of supportedContentTypes: [UTType], perform action: @escaping (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent
```

#### Return Value

A view that calls `action` when elements are inserted into the original view.

## Parameters

- `supportedContentTypes`: An array of UTI types that the dynamic   view supports.
- `action`: A closure that SwiftUI invokes when elements are added to   the view. The closure takes two arguments: The first argument is the   offset relative to the dynamic view’s underlying collection of data.   The second argument is an array of    items that   represents the data that you want to insert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:))*
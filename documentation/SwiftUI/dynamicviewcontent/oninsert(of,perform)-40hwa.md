# onInsert(of:perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the insert action for the dynamic view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`onInsert(of:perform:)`](./oninsert%28of,perform%29-418bq.md) instead.

## Declaration

```swift
func onInsert(of acceptedTypeIdentifiers: [String], perform action: @escaping (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent
```

**Other overloads**:

```swift
nonisolated
func onInsert(of supportedContentTypes: [UTType], perform action: @escaping (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent
```

## Return Value

A view that calls `action` when elements are inserted into the original view.

## Parameters

- `acceptedTypeIdentifiers`: An array of UTI types that the dynamic view supports.
- `action`: A closure that SwiftUI invokes when elements are added to the view. The closure takes two arguments: The first argument is the offset relative to the dynamic view’s underlying collection of data. The second argument is an array of `NSItemProvider` that represents the data that you want to insert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)-40hwa)*
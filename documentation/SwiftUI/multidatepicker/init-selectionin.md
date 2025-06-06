# init(_:selection:in:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that selects multiple dates on or after some start date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<Set<DateComponents>>, in bounds: PartialRangeFrom<Date>)
```

## Parameters

- `titleKey`: The key for the localized title of  , describing   its purpose.
- `selection`: The date values being displayed and selected.
- `bounds`: The open range from some selectable start date.

## See Also

- [init(selection:in:label:)](multidatepicker/init(selection:in:label:).md)
  Creates an instance that selects multiple dates on or after some start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/multidatepicker/init(_:selection:in:))*
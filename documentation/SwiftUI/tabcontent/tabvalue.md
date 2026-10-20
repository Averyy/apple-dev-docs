# TabValue

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type used to drive selection for the containing tab view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
associatedtype TabValue : Hashable where Self.TabValue == Self.Body.TabValue
```

## See Also

### Setting tab content
- [var body: Self.Body](./body-swift.property.md)
  The value of this type’s nested content.
- [associatedtype Body : TabContent](./body-swift.associatedtype.md)
  The type of content representing the body of this content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/tabvalue)*
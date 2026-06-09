# body

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The value of this type’s nested content.

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
@TabContentBuilder
<Self.TabValue> @MainActor @preconcurrency var body: Self.Body { get }
```

## See Also

- [associatedtype Body : TabContent](tabcontent/body-swift.associatedtype.md)
  The type of content representing the body of this content type.
- [associatedtype TabValue : Hashable](tabcontent/tabvalue.md)
  The type used to drive selection for the containing tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/body-swift.property)*
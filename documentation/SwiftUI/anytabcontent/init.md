# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Create an instance that type-erases `tabContent`.

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
init<T>(_ tabContent: T) where SelectionValue == T.TabValue, T : TabContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anytabcontent/init(_:))*
# scrollTo(id:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Scrolls the position of the scroll view to a view with a identity value and anchor you provide.

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
mutating func scrollTo(id: some Hashable & Sendable, anchor: UnitPoint? = nil)
```

#### Discussion

Inform the scroll view of which layout it should look for view’s with the identity value you provide using the [`scrollTargetLayout(isEnabled:)`](../view/scrolltargetlayout%28isenabled%29.md) modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollposition/scrollto(id:anchor:))*
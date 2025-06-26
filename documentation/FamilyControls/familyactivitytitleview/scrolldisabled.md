# scrollDisabled(_:)

**Framework**: FamilyControls  
**Kind**: method

Disables or enables scrolling in scrollable views.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func scrollDisabled(_ disabled: Bool) -> some View
```

#### Discussion

Use this modifier to control whether a `ScrollView` can scroll:

```swift
@State private var isScrollDisabled = false

var body: some View {
    ScrollView {
        VStack {
            Toggle("Disable", isOn: $isScrollDisabled)
            MyContent()
        }
    }
    .scrollDisabled(isScrollDisabled)
}
```

SwiftUI passes the disabled property through the environment, which means you can use this modifier to disable scrolling for all scroll views within a view hierarchy. In the following example, the modifier affects both scroll views:

```swift
 ScrollView {
     ForEach(rows) { row in
         ScrollView(.horizontal) {
             RowContent(row)
         }
     }
 }
 .scrollDisabled(true)
```

You can also use this modifier to disable scrolling for other kinds of scrollable views, like a `List` or a `TextEditor`.

## Parameters

- `disabled`: A Boolean that indicates whether scrolling is   disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/scrolldisabled(_:))*
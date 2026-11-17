# scrollDisabled(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Disables or enables scrolling in scrollable views.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func scrollDisabled(_ disabled: Bool) -> some View
```

## Discussion

Use this modifier to control whether a [`ScrollView`](../scrollview.md) can scroll:

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

SwiftUI passes the disabled property through the environment, which means you can use this modifier to disable scrolling for the scroll views within a view hierarchy. A scroll view doesn’t pass the disabled property to the scroll views nested inside it. In the following example, the modifier disables only the outer scroll view; the nested scroll views remain enabled unless you also apply the modifier to them:

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

You can also use this modifier to disable scrolling for other kinds of scrollable views, like a [`List`](../list.md) or a [`TextEditor`](../texteditor.md).

## Parameters

- `disabled`: A Boolean that indicates whether scrolling is disabled.

## See Also

### Disabling scrolling
- [var isScrollEnabled: Bool](../environmentvalues/isscrollenabled.md)
  A Boolean value that indicates whether any scroll views associated with this environment allow scrolling to occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolldisabled(_:))*
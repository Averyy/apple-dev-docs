# pageCommand(value:in:step:)

**Framework**: MusicKit  
**Kind**: method

Steps a value through a range in response to page up or page down commands.

**Availability**:
- tvOS 14.3+

## Declaration

```swift
nonisolated
func pageCommand<V>(value: Binding<V>, in bounds: ClosedRange<V>, step: V = 1) -> some View where V : BinaryInteger
```

#### Discussion

Use this command to step through sections of a data model associated with a view by providing a binding to a value, a range, and step. If taking another step would cause the value to exceed the bounds, then the value remains unchanged.

On tvOS, the user triggers ‘pageUp’ and ‘pageDown’ commands by pressing a dedicated button on a connected remote. For example, you can let a user page through a TV programming guide using the channel buttons:

```swift
struct GuideView: View {
    @State private var pageOffset: Int = 0

    var body: some View {
        GuideContent(at: pageOffset)
            .pageCommand(
                value: $pageOffset,
                in: 0...9,
                step: 1)
    }
}
```

## Parameters

- `value`: A   to the value to modify when the user pages   up or down.
- `bounds`: A closed range that specifies the upper and lower   bounds of  .
- `step`: The amount by which to increment or decrement  .   Defaults to 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/pagecommand(value:in:step:))*
# presentationBreakthroughEffect(_:)

**Framework**: Assignables  
**Kind**: method

Changes the way the enclosing presentation breaks through content occluding it.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func presentationBreakthroughEffect(_ effect: BreakthroughEffect) -> some View
```

#### Discussion

Use this modifier to disable or customize a breakthrough effect for the enclosing presentation.

Breakthrough is an effect allowing elements to be visible to the user even when other app content (3D models, UI elements) is occluding it. The way the element appears depends on the chosen `BreakthroughEffect`.

Most system presentations appear with a breakthrough effect by default. For these cases, the `presentationBreakthroughEffect` modifier allows customization of the type of effect. This is achieved by applying the modifier to the content of the presentation:

```swift
Button("Show Details") {
    isShowingDetails = true
}
.popover(isPresented: $isShowingDetails) {
    DetailsView()
        .presentationBreakthroughEffect(.prominent)
}
```

Only popovers allow breakthrough to be disabled altogether. Passing a `.none` value for a sheet doesn’t have any effect.

## Parameters

- `effect`: The type of effect to apply when a presentation element is   occluded by other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/presentationbreakthrougheffect(_:))*
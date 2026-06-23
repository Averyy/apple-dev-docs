# crossFade

**Framework**: SwiftUI  
**Kind**: property

A navigation transition that cross-fades between the appearing view and the disappearing view.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var crossFade: CrossFadeNavigationTransition { get }
```

#### Discussion

Specify this transition in a sheet to have it appear by fading in over the content, as opposed to moving upwards to cover content.

This example shows a sheet that appears with a cross-fade.

```swift
struct ContentView: View {
    @State private var showSheet = false

    var body: some View {
        VStack {
            Button("Show Sheet") {
                showSheet = true
            }
            .sheet(isPresented: $showSheet) {
                Text("Sheet Content")
                    .presentationDetents([.medium])
                    .navigationTransition(.crossFade)
            }
        }
    }
}
```

## See Also

- [static var automatic: AutomaticNavigationTransition](navigationtransition/automatic.md)
  A style that automatically chooses the appropriate presentation transition for the current context.
- [struct AutomaticNavigationTransition](automaticnavigationtransition.md)
  A style that automatically chooses the appropriate presentation transition for the current context.
- [struct CrossFadeNavigationTransition](crossfadenavigationtransition.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.
- [static func zoom(sourceID: some Hashable, in: Namespace.ID) -> ZoomNavigationTransition](navigationtransition/zoom(sourceid:in:).md)
  A navigation transition that zooms the appearing view from a given source view.
- [struct ZoomNavigationTransition](zoomnavigationtransition.md)
  A navigation transition that zooms the appearing view from a given source view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationtransition/crossfade)*
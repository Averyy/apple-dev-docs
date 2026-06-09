# AnyNavigationTransition

**Framework**: SwiftUI  
**Kind**: struct

A type-erasing navigation transition that allows for providing any navigation transition value dynamically.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AnyNavigationTransition
```

#### Overview

Use this navigation transition when you need to dynamically configure the transition of your content. For example, you could use this in a [`sheet(isPresented:onDismiss:content:)`](view/sheet(ispresented:ondismiss:content:).md) modifier to dynamically configure how the sheet transitions in and out.

This example shows a sheet that uses a different transition based on model state.

```swift
struct ContentView: View {
    @State private var showSheet = false
    @Environment(Model.self) var model

    var body: some View {
        VStack {
            Button("Show Sheet") {
                showSheet = true
            }
            .sheet(isPresented: $showSheet) {
                let transition = model.useCrossDissolve
                    ? AnyNavigationTransition(.crossFade)
                    : AnyNavigationTransition(.automatic)
                Text("Sheet Content")
                    .presentationDetents([.medium])
                    .navigationTransition(transition)
            }
        }
    }
}
```

## Topics

### Initializers
- [init(some NavigationTransition)](anynavigationtransition/init(_:).md)

## Relationships

### Conforms To
- [NavigationTransition](navigationtransition.md)

## See Also

- [func navigationTransition(some NavigationTransition) -> some View](view/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [protocol NavigationTransition](navigationtransition.md)
  A type that defines the transition to use when navigating to a view.
- [struct CrossFadeNavigationTransition](crossfadenavigationtransition.md)
  A navigation transition that cross-fades between the appearing view and the disappearing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anynavigationtransition)*
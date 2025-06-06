# Adding a background to your view

**Framework**: SwiftUI

Compose a background behind your view and extend it beyond the safe area insets.

#### Overview

You can add a view as a background with the [`background(_:alignment:)`](view/background(_:alignment:).md) view modifier. To add a background under multiple views, or to have a background larger than an existing view, you can layer the views by placing them within a [`ZStack`](zstack.md), and place the view you want to be in the background at the bottom of the view stack. You can specify that a background view should ignore the safe area insets to extend the background to some or all edges.

##### Add a Background

If your design calls for a background, you can use the [`background(_:alignment:)`](view/background(_:alignment:).md) modifier to add it underneath an existing view. The following example adds a gradient to the vertical stack using the [`background(_:alignment:)`](view/background(_:alignment:).md) view modifier:

```swift
let backgroundGradient = LinearGradient(
    colors: [Color.red, Color.blue],
    startPoint: .top, endPoint: .bottom)

struct SignInView: View {
    @State private var name: String = ""

    var body: some View {
        VStack {
            Text("Welcome")
                .font(.title)
            HStack {
                TextField("Your name?", text: $name)
                    .textFieldStyle(.roundedBorder)
                Button(action: {}, label: {
                    Image(systemName: "arrow.right.square")
                        .font(.title)
                })
            }
            .padding()
        }
        .background(backgroundGradient)
    }
}
```

The [`background(_:alignment:)`](view/background(_:alignment:).md) view modifier constrains the size of the background view to be the same size as the view to which it’s attached:

![A screenshot of an iPhone showing a gradient background for the welcome title, text field, and button in the horizontal stack, not filling in the rest of the phone’s background.](https://docs-assets.developer.apple.com/published/0bf57a769f3fffece6ad3746e6189c9b/Adding-a-Background-to-Your-View-1%402x.png)

##### Expand the Background Underneath Your View

To create a background that’s larger than the vertical stack, use a different technique. You could add [`Spacer`](spacer.md) views above and below the content in the [`VStack`](vstack.md) to expand it, but that would also expand the size of the stack, possibly changing it’s layout. To add in a larger background without changing the size of the stack, nest the views within a [`ZStack`](zstack.md) to layer the [`VStack`](vstack.md) over the background view:

```swift
struct SignInView: View {
    @State private var name: String = ""

    var body: some View {
        ZStack {
            backgroundGradient
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
    }
}
```

View sizes within a depth stack are independent, unlike when using the background view modifier. The view from [`Gradient`](gradient.md) expands to fill the space available to the stack, but avoids the safe area insets by default:

![A screenshot of an iPhone showing a gradient background filling almost all of the background, excluding the top status bar and the bottom bar.](https://docs-assets.developer.apple.com/published/28c3048a58718732a59c8d93b16cf7eb/Adding-a-Background-to-Your-View-2%402x.png)

For more information on usings stacks to combine views, see [`Building layouts with stack views`](building-layouts-with-stack-views.md).

##### Extend the Background Into the Safe Areas

By default, SwiftUI sizes and positions views to avoid system defined safe areas to ensure that system content or the edges of the device won’t obstruct your views. If your design calls for the background to extend to the screen edges, use the [`ignoresSafeArea(_:edges:)`](view/ignoressafearea(_:edges:).md) modifier to override the default.

```swift
struct SignInView: View {
    @State private var name: String = ""
    var body: some View {
        ZStack {
            backgroundGradient
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
        .ignoresSafeArea()
    }
}
```

The background gradient fills the display area of the device and ignores the safe area insets.

![A screenshot of an iPhone showing a gradient background filling the entire background.](https://docs-assets.developer.apple.com/published/412380a0db85bd69c4d78c41bc8bf147/Adding-a-Background-to-Your-View-3%402x.png)

##### Adjust Views When Displaying the Keyboard

You can ignore the keyboard’s safe area by adding the [`ignoresSafeArea(_:edges:)`](view/ignoressafearea(_:edges:).md) modifier. When you activate the keyboard, the content of the vertical stack remains fixed, ignoring the space used by the keyboard:

![A screenshot of an iPhone showing a gradient background filling the entire background, with the keyboard overlaid at the bottom of the screen. The welcome title, text field, and button within the horizontal stack are centered between the top and bottom of the iPhone, with the keyboard obscuring the lower portion of the background.](https://docs-assets.developer.apple.com/published/dbcdefbeadfd2a3fd95589b4e72b7eb6/Adding-a-Background-to-Your-View-4%402x.png)

To get the contents of the vertical stack to respect the safe areas and adjust to the keyboard, move the modifier to only apply to the background view.

```swift
struct SignInView: View {
    @State private var name: String = ""
    var body: some View {
        ZStack {
            backgroundGradient
                .ignoresSafeArea()
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
    }
}
```

To accommodate the keyboard, SwiftUI resizes and positions your view. Because the background view has the [`ignoresSafeArea(_:edges:)`](view/ignoressafearea(_:edges:).md) modifier, it remains unchanged.

![A screenshot of an iPhone showing a gradient background filling the entire background, with the keyboard overlaid at the bottom of the screen. The welcome title, text field, and button within the horizontal stack is centered between the top of the keyboard and the top of the iPhone, and the gradient background extends underneath the keyboard for the full height of the iPhone.](https://docs-assets.developer.apple.com/published/6efd7980ea4347e5b74de09f0907c406/Adding-a-Background-to-Your-View-5%402x.png)

## See Also

- [struct ZStack](zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](view/zindex(_:).md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](view/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](view/background(_:in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](view/background(in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](view/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](view/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [var backgroundMaterial: Material?](environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](view/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](view/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [struct ContainerBackgroundPlacement](containerbackgroundplacement.md)
  The placement of a container background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/adding-a-background-to-your-view)*
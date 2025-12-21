# init(make:update:placeholder:)

**Framework**: RealityKit  
**Kind**: init

Creates a reality view for iOS and macOS, with an optional update closure and placeholder view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
nonisolated
init<P>(make: @escaping @MainActor (inout RealityViewCameraContent) async -> Void, update: (@MainActor (inout RealityViewCameraContent) -> Void)? = nil, @ViewBuilder placeholder: () -> P) where Content == RealityViewCameraContent.Body<P>, P : View
```

#### Discussion

For example, your app can asynchronously load an [`Entity`](entity.md) from a `.reality` or `.usdz` file, and display a [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView) while the system loads the file:

```swift
RealityView { content in
    if let newEntity = try? await Entity(named: "model_file_name") {
        content.add(newEntity)
    }
} placeholder: {
    ProgressView()
}
```

## Parameters

- `make`: An asynchronous closure that configures the   initial content of the new  .   This closure is asynchronous to keep your app’s UI responsive while   you load content to populate this view.
- `update`: An optional closure that updates the    instance’s content as the view’s state changes.
- `placeholder`: A temporary view that the   displays until   your closure for the   parameter completes.   For example, you can display a loading indicator with a     instance as a placeholder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/init(make:update:placeholder:))*
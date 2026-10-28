# init(make:update:placeholder:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a new reality view for visionOS with an optional update closure and placeholder view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<P>(make: @escaping @MainActor @Sendable (inout RealityViewContent) async -> Void, update: (@MainActor (inout RealityViewContent) -> Void)? = nil, @ViewBuilder placeholder: () -> P) where Content == RealityViewContent.Body<P>, P : View
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<P>(make: @escaping @MainActor @Sendable (inout RealityViewCameraContent) async -> Void, update: (@MainActor (inout RealityViewCameraContent) -> Void)? = nil, @ViewBuilder placeholder: () -> P) where Content == RealityViewCameraContent.Body<P>, P : View
```

## Discussion

For example, your app can asynchronously load an [`Entity`](../entity.md) from a `.reality` or `.usdz` file, and display a [`ProgressView`](../../SwiftUI/progressview.md) while the system loads the file:

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

- `make`: An asynchronous closure that configures the initial content of the new `RealityView`. This closure is asynchronous to keep your app’s UI responsive while you load content to populate this view.
- `update`: An optional closure that updates the `RealityView` instance’s content as the view’s state changes.
- `placeholder`: A temporary view that the [`RealityView`](../realityview.md) displays until your closure for the `make` parameter completes. For example, you can display a loading indicator with a [`ProgressView`](../../SwiftUI/progressview.md) instance as a placeholder.

## See Also

### Creating a reality view for visionOS
- [init(make: (inout RealityViewContent) async -> Void, update: ((inout RealityViewContent) -> Void)?)](./init%28make,update%29-666xr.md)
  Creates a new reality view for visionOS with an optional update closure.
- [init<A>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, attachments: () -> A)](./init%28make,update,attachments%29.md)
  Creates a reality view for visionOS, with attachments and an optional update closure.
- [init<A, P>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, placeholder: () -> P, attachments: () -> A)](./init%28make,update,placeholder,attachments%29.md)
  Creates a reality view for visionOS, with attachments, an optional update closure, and placeholder view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/init(make:update:placeholder:)-4c8yv)*
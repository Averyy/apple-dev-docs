# init(make:update:placeholder:)

**Framework**: RealityKit  
**Kind**: init

Creates a new reality view for visionOS with an optional update closure and placeholder view.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<P>(make: @escaping @MainActor (inout RealityViewContent) async -> Void, update: (@MainActor (inout RealityViewContent) -> Void)? = nil, @ViewBuilder placeholder: () -> P) where Content == RealityViewContent.Body<P>, P : View
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

## See Also

- [init(make: (inout RealityViewContent) async -> Void, update: ((inout RealityViewContent) -> Void)?)](realityview/init(make:update:)-666xr.md)
  Creates a new reality view for visionOS with an optional update closure.
- [init<A>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, attachments: () -> A)](realityview/init(make:update:attachments:).md)
  Creates a reality view for visionOS, with attachments and an optional update closure.
- [init<A, P>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, placeholder: () -> P, attachments: () -> A)](realityview/init(make:update:placeholder:attachments:).md)
  Creates a reality view for visionOS, with attachments, an optional update closure, and placeholder view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/init(make:update:placeholder:)-4c8yv)*
# dropConfiguration(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures a drop session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dropConfiguration(_ configuration: @escaping (DropSession) -> DropConfiguration) -> some View
```

#### Return Value

A view that configures a drop session in a way, described by the `configuration` parameter.

#### Discussion

Below is an example of a view that accepts drop of `Image` type. The view prefers drop operation move in a case when the source suppots it (the source will remove the images from its storage after the drop operation). If the source does not support moving images, the destination will make copies.

```swift
       ExampleView()
           .dropDestination(for: Image.self) { images, _ in
               process(images)
           }
           .dropConfiguration { dropSession in
               if dropSession.suggestedOperations.contains(.move) {
                   return DropConfiguration(operation: .move)
               }
               return DropConfiguration(operation: .copy)
           }
```

## Parameters

- `configuration`: A value that describes the cofiguration   of a drop session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dropconfiguration(_:))*
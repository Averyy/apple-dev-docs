# realityViewLayoutBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

A view modifier that controls the frame sizing and content alignment behavior for `RealityView`

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func realityViewLayoutBehavior(_ layoutOption: RealityViewLayoutOption) -> some View
```

#### Discussion

This modifier is only accounted for after the end of the `make` closure. It isn’t checked on any calls to the `update` closure.

```swift
    struct ModelWrapperView: View {
        let modelName: String
        var body: some View {
            RealityView { content in
                let model = try? await Entity(named: modelName)
                if let model {
                    content.add(model)
                }
            }
            .realityViewLayoutBehavior(.fixedSize)
        }
    }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/realityviewlayoutbehavior(_:))*